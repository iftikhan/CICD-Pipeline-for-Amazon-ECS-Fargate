import logging
from motor.motor_asyncio import AsyncIOMotorClient
from .mongodb import db
import os
from databases import DatabaseURL
from database.config import MONGODB_URL, MAX_CONNECTIONS_COUNT, MIN_CONNECTIONS_COUNT



# MONGODB_URL = os.getenv("MONGODB_URL", "")  # deploying without docker-compose

# if not MONGODB_URL:
#     MONGO_HOST = os.getenv("MONGO_HOST", "localhost")
#     MONGO_PORT = int(os.getenv("MONGO_PORT", 27017))
#     MONGO_USER = os.getenv("MONGO_USER", "admin")
#     MONGO_PASS = os.getenv("MONGO_PASSWORD", "markqiu")
#     MONGO_DB = os.getenv("MONGO_DB", "fastapi")

#     MONGODB_URL = DatabaseURL(
#         f"mongodb://{MONGO_USER}:{MONGO_PASS}@{MONGO_HOST}:{MONGO_PORT}/{MONGO_DB}"
#     )
# else:
#     MONGODB_URL = DatabaseURL(MONGODB_URL)

async def connect_to_mongo():
    logging.info("connecting...")
    db.client = AsyncIOMotorClient(str(MONGODB_URL),
                                    maxPoolSize = MAX_CONNECTIONS_COUNT,
                                    minPoolSize =MIN_CONNECTIONS_COUNT)
    logging.info("connected!")


async def close_mongo_connection():
    logging.info("Closing...")
    db.client.close()
    logging.info("Closed!")