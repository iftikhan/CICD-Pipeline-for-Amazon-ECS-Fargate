import database
from motor.motor_asyncio import AsyncIOMotorClient
from odmantic.engine import AIOEngine


class DataBase:
    client: AsyncIOMotorClient = None
   

db = DataBase()


async def get_database() -> AsyncIOMotorClient:
    return db.client