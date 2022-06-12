from re import A, U
from fastapi import FastAPI, HTTPException, File, UploadFile
from typing import Collection, List
from fastapi.param_functions import Depends, Form
from odmantic.bson import ObjectId
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder
import motor
from motor.motor_asyncio import AsyncIOMotorClient
from odmantic import AIOEngine
import json
from datetime import date, datetime, timedelta
# from database.database import Db
from app.login.login_model import user_login
from app.login.login_model_update import user_login_update
from app.login.auth import AuthHandler
from fastapi.security import OAuth2PasswordRequestForm


app = FastAPI()
client = AsyncIOMotorClient("mongodb://admin:admin@mongoserver:27017/")
engine = AIOEngine(motor_client=client, database="customer_base")
app.add_middleware(
    CORSMiddleware,    
    allow_origins=["*"],    
    allow_methods=["*"],    
    allow_headers=["*"],    
    allow_credentials=True,   
)



auth_handler = AuthHandler()


@app.post('/register_user',response_model= user_login, tags = ["user_login"])
async def register_user(auth_detail: user_login):
    if await engine.find_one(user_login, user_login.username == auth_detail.username):
        raise HTTPException(status_code=400, detail= "Username is taken")

    hashed_password = auth_handler.get_password_hashed(auth_detail.password)
    auth_detail.password = hashed_password
    await engine.save(auth_detail)
    return auth_detail


@app.post('/login', tags=["user_login"])
async def login(username: str= Form(...), password : str = Form(...)):
    users = None
    user = await engine.find_one(user_login, user_login.username == username)
    # for each in len(user):
    #     print(each)
    print(type(user))
    if user.username == username:
        users = user.username

    if (users is None) or (not auth_handler.verify_password(password, user.password)):
        raise HTTPException(status_code=401, detail= 'Invalid username and/or password')
    
    token = auth_handler.encode_token(username)
    return {"token":token, 'userid':user}




@app.get("/user_login",response_model= List[user_login],tags = ["user_login"])
async def get_user(form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    trees = await engine.find(user_login)
    return trees

@app.get("/user_login_by/{id}", response_model=user_login,tags = ["user_login"])
async def get_user_login_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree = await engine.find_one(user_login, user_login.id == id)
    if tree is None:
        raise HTTPException(404)
    return tree

@app.delete("/user_login/{id}", response_model=user_login,tags = ["user_login"])
async def delete_user_login_by_id(id: ObjectId,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree = await engine.find_one(user_login, user_login.id == id)
    if tree is None:
        raise HTTPException(404)
    await engine.delete(tree)
    return tree

#@app.patch("/user_login/{id}", response_model=user_login,tags = ["user_login"])
async def update_user_login_by_id(id: ObjectId, patch: user_login_update,form_data: OAuth2PasswordRequestForm = Depends(auth_handler.auth_wraper)):
    tree = await engine.find_one(user_login, user_login.id == id)
    if tree is None:
        raise HTTPException(404)
    patch_dict = patch.dict(exclude_unset=True)
    for name, value in patch_dict.items():
        setattr(tree, name, value)
    await engine.save(tree)
    return tree

