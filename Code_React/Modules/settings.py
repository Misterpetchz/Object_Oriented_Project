
from typing import Optional
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from datetime import timedelta, datetime
from jose import JWTError, jwt
from passlib.context import CryptContext
import gc
import json
import hashlib

SECRET_KEY = "0ecb3c3265b8073a4686a79606109099c6116152a390597514c9eff447fb1f94"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTE = 30
PWD_CONTEXT = CryptContext(schemes=["bcrypt"], deprecated="auto")
OAUTH2_SCHEME = OAuth2PasswordBearer(tokenUrl="token")

class Token(BaseModel) :
	access_token : str
	token_type : str
class TokenData(BaseModel) :
	email : str or None = None

# ! Legacy Code (Break the OOP Principal) DO NOT USE!!
# def	InstanceFinder(classType, attribute, Target) :
# 	for obj in gc.get_objects() :
# 		if isinstance(obj, classType) and getattr(obj, attribute) == Target :
# 			return (obj)
# 	return (None);

def	ClassInstancePacker(classType) :
	instance_list = []
	for obj in gc.get_objects() :
		if isinstance(obj, classType) :
			instance_list.append(obj)
	return (instance_list)
