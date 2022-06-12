from typing import Collection, List, Optional, Union
from datetime import date, datetime, timezone
from odmantic import AIOEngine, Model, ObjectId,Reference, Field
from pydantic import BaseModel




class user_login(Model):
    username : str
    password : str
    email: str
    firstname : str
    lastname: str
    createdAt : datetime = Field(default_factory=datetime.utcnow)
    updatedAt : datetime = Field(default_factory=datetime.utcnow)

    class Config:
        collection = "user_login"

