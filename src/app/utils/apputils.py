import json
import logging
import sys
import traceback
from datetime import datetime
from typing import Any

import jinja2
import pdfkit
from botocore.exceptions import ClientError

from config import Config

logging.getLogger().setLevel(logging.INFO)
logger = logging.getLogger("generate_compliance_report_utils")


def get_s3_object_data(bucket_name: str, object_key: str) -> Any:
    """
    Gets data from s3 location
    """
    logger.info(f"Getting s3://{bucket_name}/{object_key} data")

    get_object = Config.client_s3.get_object(Bucket=bucket_name, Key=object_key)
    file_content = get_object["Body"].read()
    return file_content


def save_data_to_s3(data: dict, bucket_name: str, identifier: str) -> None:
    """

    :param data:
    :param bucket_name:
    :param identifier:
    """
    logger.info(f"save_data_to_s3 {bucket_name}, {identifier}")
    Config.client_s3.put_object(
        Body=json.dumps(data),
        ContentType="application/json",
        Bucket=bucket_name,
        Key=f"{identifier}.json",
    )


def save_pdf_to_s3(report_bucket_name: str, pdf_identifier: str) -> None:
    logger.info(f"save_pdf_to_s3 with {report_bucket_name} and  {pdf_identifier}")
    key = f"{pdf_identifier}"
    Config.client_s3.put_object(
        Body=open(f"/tmp/{pdf_identifier}.pdf", "rb"),
        ContentType="application/pdf",
        Bucket=report_bucket_name,
        Key=f"{key}.pdf",
    )


def get_object_list(bucket: str) -> list:
    """
    Gets list of object in a given bucket and prefix
    """
    logger.info(f"Getting list of bucket {bucket}")

    list_of_objects = []
    paginator = Config.resource_s3.meta.client.get_paginator("list_objects")
    for result in paginator.paginate(Bucket=bucket):
        if "Contents" in result:
            s3_object = [f["Key"] for f in result["Contents"]]
            list_of_objects.extend(s3_object)
    return list_of_objects


def generate_link(bucket_name: str, key: str, public=False) -> str:
    """

    :rtype: object
    """
    logger.info(f"generate_link with {bucket_name}, {key},{public}")
    if public:
        pdf_link = Config.client_s3.generate_presigned_url(
            ClientMethod="get_object",
            Params={"Bucket": bucket_name, "Key": f"{key}.pdf"},
            ExpiresIn=Config.EXPIRES_IN,
        )
    else:
        pdf_link = f"https://s3.console.aws.amazon.com/s3/buckets/{bucket_name}?prefix={key}.pdf"
    return pdf_link


def notifier(report_identifier: str, link: str) -> None:
    """
    Report Notifier.
    """
    message = f"Compliance report of {report_identifier} is as below. \n\n{link}\n\n\n"

    logger.info(message)
    try:
        Config.sns_client.publish(
            TargetArn=Config.sns_error_topic_arn,
            Subject=f"Compliance report of {report_identifier}",
            Message=message,
        )
    except ClientError:
        ex_type, ex, tb = sys.exc_info()
        error = {"type": str(ex_type), "ex": str(ex), "stack": traceback.format_exc()}
        logger.error(error)
        auto_iq_exception(json.dumps(error))


def auto_iq_exception(exception: str) -> None:
    """
    Global Exception handler to pass this information to error topic.
    """
    try:
        logger.error(exception)
        Config.sns_client.publish(
            TargetArn=Config.sns_error_topic_arn,
            Subject="Error/Exception in generate_compliance_report_lambda",
            Message=exception,
        )
    except ClientError as e:
        logger.error("An error occurred: %s" % e)


def convert_empty_values(d: Any) -> Any:
    """
    Removed
    """
    for k in d:
        if isinstance(d[k], dict):
            convert_empty_values(d[k])
        elif isinstance(d[k], list):
            for i in range(0, len(d[k])):
                if isinstance(d[k][i], list) or isinstance(d[k][i], dict):
                    convert_empty_values(d[k][i])
                elif isinstance(d[k][i], float):
                    d[k][i] = str(d[k][i])
        elif d[k] == "":
            d[k] = None
        elif isinstance(d[k], datetime):
            d[k] = d[k].isoformat()
        elif isinstance(d[k], float):
            d[k] = str(d[k])
    return d


def generate_html(
        pdf_name: str, template: str, data: dict, search_path: str, tmp_loc="/tmp"
) -> None:
    """
    This Function will generate html file form jinja and then convert file to pdf
    :param pdf_name:
    :param template:
    :param data:
    :param search_path:
    :param tmp_loc:
    """

    logger.info("Setting up jinja")
    template_loader = jinja2.FileSystemLoader(searchpath=search_path)
    template_env = jinja2.Environment(
        loader=template_loader, extensions=["jinja2.ext.do"], autoescape=True
    )

    template = template_env.get_template(f"{template}.html")
    template_env.globals.update(zip=zip)

    logger.info("Rendering jinja template")
    output_text = template.render(
        data=data, created_time=datetime.utcnow().strftime("%Y-%m-%d")
    )

    logger.info("Saving generated file in temp location")
    with open(f"{tmp_loc}/{pdf_name}.html", "w+") as html_file:
        html_file.write(output_text)


def generate_pdf(
        pdf_name: str, template: str, search_path: str, tmp_loc="/tmp"
) -> None:
    """
    This Function will generate html file form jinja and then convert file to pdf
    :param pdf_name:
    :param template:
    :param search_path:
    :param tmp_loc:
    """
    logger.info(f"generate_pdf with {pdf_name},{template}")

    logger.info("Setting up pdf kit configuration")
    pdf_conf = pdfkit.configuration()
    options = {
        "--header-html": f"{tmp_loc}/{pdf_name}-header.html",
        "--footer-html": f"{search_path}/default-compliance-template-footer.html",
    }
    logger.info("Converting HTML to pdf")
    pdfkit.from_file(
        f"{tmp_loc}/{pdf_name}.html",
        f"{tmp_loc}/{pdf_name}.pdf",
        configuration=pdf_conf,
        options=options,
    )

    logger.info("generate_pdf pdf generated and stored on temp location")


def save_data_to_dynamodb(data: dict, table_name: str) -> None:
    """

    :param data:
    :param table_name:
    """
    logger.info(f"save_data_to_dynamodb with table_name: {table_name}")
    table = Config.dynamodb.Table(table_name)
    table.put_item(Item=convert_empty_values(data))


def get_item_from_dynamodb_by_key(key: Any, table_name: str) -> dict:
    """

    :param key:
    :param table_name:
    """
    logger.info(f"get_item_from_dynamodb_by_key with {key},{table_name}")
    table = Config.dynamodb.Table(table_name)
    return table.get_item(Key={Config.table_primary_key: key})["Item"]


def send_ecs_task_success(output: str, task_token: str = Config.task_token) -> None:
    """

    :param task_token:
    """
    logger.info("Send Step function success response")
    Config.sfn_client.send_task_success(taskToken=task_token, output=output)


def send_ecs_task_failure(
        cause: str, error: str, task_token: str = Config.task_token
) -> None:
    """
    :param cause:
    :param error:
    :param task_token:
    """
    logger.info("Send Step function failure response")
    Config.sfn_client.send_task_failure(cause=cause, error=error, taskToken=task_token)


def get_parameter(param_name: str, is_secured: object = True) -> str:
    """

    :param param_name:
    :param is_secured:
    """
    logger.info(f"Getting SSM parameter: {param_name}")
    response = Config.ssm_client.get_parameter(
        Name=param_name, WithDecryption=is_secured
    )
    _data = response["Parameter"].get("Value")
    try:
        _data = json.loads(_data)
    except ValueError:
        pass

    return _data
