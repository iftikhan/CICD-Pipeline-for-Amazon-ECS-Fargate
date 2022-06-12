import motor
from motor.motor_asyncio import AsyncIOMotorClient
from odmantic import AIOEngine

class Db:
    client = AsyncIOMotorClient('mongodb://admin:admin@mongoserver:27017')
    engine = AIOEngine(motor_client=client, database="ehadaya")

