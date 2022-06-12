from time import tzname
from typing import Optional
from odmantic.bson import ObjectId
from pydantic import BaseModel, Field
from datetime import datetime, time, timedelta,timezone
from typing import Collection, List, Optional, Union
from datetime import date, datetime, timezone
from odmantic import AIOEngine, Model, ObjectId,Reference, Field, model
from starlette.requests import cookie_parser


class user_login_update(BaseModel):
    username :Optional[str]
    password : Optional[str]
    email: Optional[str]
    firstname : Optional[str]
    lastname: Optional[str]

    class Config:
        collection = "user_login_update"