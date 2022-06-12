import logging
import os
import sys

import boto3


class BaseConfig:
    # AWS Configurations
    aws_region = os.getenv("AWS_REGION", "us-west-2")

    # Global Variables
    sns_error_topic_arn = os.getenv("SNS_ERROR_TOPIC", "SNS_ERROR_TOPIC_NOT_SET")
    connection_string_path = os.getenv("DB_CONNECTION_STR", "DB_CONNECTION_STR_NOT_SET")
    sns_error_topic = os.getenv("SNS_ERROR_TOPIC", "SNS_ERROR_TOPIC_NOT_SET")
    raw_data_bucket = os.getenv("RAW_DATA_BUCKET", "RAW_DATA_BUCKET_NOT_SET")

    #  Clients
    client_s3 = boto3.client("s3", region_name=aws_region)
    resource_s3 = boto3.resource("s3", region_name=aws_region)
    sns_client = boto3.client("sns", region_name=aws_region)
    ssm_client = boto3.client("ssm", region_name=aws_region)

    log_level = logging.INFO
    log_stream = sys.stderr

    # Constants
    EXPIRES_IN = 60 * 60 * 24 * 7
    template_location = "./template/"


class TestingConfig(BaseConfig):
    pass


class DevelopmentConfig(BaseConfig):
    pass


class ProductionConfig(BaseConfig):
    pass


class GossConfig(BaseConfig):
    dummy_response = True


def get_config():
    # Setting LAMBDA_ENVIRONMENT to GOSS to get around Docker test
    env = os.getenv("LAMBDA_ENVIRONMENT", "GOSS")

    if env == "GOSS":
        return GossConfig()

    if env == "TEST":
        return TestingConfig()

    if env == "DEVELOP":
        return DevelopmentConfig()

    if env == "PROD":
        return ProductionConfig()

    raise EnvironmentError(
        f"Environment variable LAMBDA_ENVIRONMENT has unrecognized value {str(env)}"
    )


Config = get_config()
