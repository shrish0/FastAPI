from fastapi import APIRouter
from models.model import User
from bson import ObjectId
from config.db import conn

from schemas.schema import userEntity,usersEntity

user = APIRouter()

@user.get('/')
async def find_all_users():
    return usersEntity(conn.local.Bright.find())


@user.post('/')
async def create_user(user:User):
    conn.local.Bright.insert_one(dict(user))
    return usersEntity(conn.local.users.find())

@user.put('/{id}')
async def update_user(id,user:User):
    conn.local.Bright.find_one_and_update({"_id":ObjectId(id)},
                                         { "$set" : dict(user)}
                                         )
    return userEntity(conn.local.Bright.find_one({"_id":ObjectId(id)}))

@user.delete('/{id}')
async def delete_user(id):
    return conn.local.Bright.find_one_and_delete({"_id":ObjectId(id)})
    