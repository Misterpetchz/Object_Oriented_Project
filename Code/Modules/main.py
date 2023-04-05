	#? External Lib
from typing import Optional
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext
import gc
from Modules.UserAccount import *

SECRET_KEY = "0ecb3c3265b8073a4686a79606109099c6116152a390597514c9eff447fb1f94"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTE = 30
PWD_CONTEXT = CryptContext(schemes=["bcrypt"], deprecated="auto")
OAUTH2_SCHEME = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI()

db = {
	"Medkit101@gmail.com" : {
		"email" : "Medkit101@gmail.com",
		"full_name" : "Dante Durante",
		"gender" : "Unknown",
		"tel" : "101564",
		"address" : "District 7",
		"email_noti" : True,
		"sms_noti" : True,
		"disabled" : False,
		"hashed_password" : "$2b$12$71C2.b9fJlp.3903g3klI.m8aIC4hRyurIX8ANpqoyWfA9QIAQ/82"
	},
	"Test101@gmail.com" : {
		"email" : "Test101@gmail.com",
		"full_name" : "Dante Durante",
		"gender" : "Unknown",
		"tel" : "101564",
		"address" : "District 7",
		"email_noti" : True,
		"sms_noti" : True,
		"disabled" : False,
		"hashed_password" : "$2b$12$b4rMellphLAUtntHySUkbexQ/IqSNba1KDEATosuU/lOKpBofIb8G"
	},
	"Test202@gmail.com" : {
		"email" : "Test202@gmail.com",
		"full_name" : "Dante Durante",
		"gender" : "Unknown",
		"tel" : "101564",
		"address" : "District 7",
		"email_noti" : True,
		"sms_noti" : True,
		"disabled" : False,
		"hashed_password" : "$2b$12$AqhPzCx2ELR29n5iVVsiSuz94XDAX.hkjQf6f4KoEjYYAXLJj/85W"
	},
}

class Token(BaseModel) :
	access_token : str
	token_type : str
class TokenData(BaseModel) :
	email : str or None = None
# class User(BaseModel) :
# 	email : str
# 	full_name : str or None = None
# 	gender : str or None = None
# 	tel : str or None = None
# 	address : str or None = None
# 	email_noti : bool or None = None
# 	sms_noti : bool or None = None
# 	disabled : bool or None = NoneV

# class UserInDB(Customer) :
# 	hashed_password : str

# def verify_password(plain_password, hashed_password) :
# 	return PWD_CONTEXT.verify(plain_password, hashed_password)

# def get_password_hash(password) :
# 	return PWD_CONTEXT.hash(password)

# def get_user(db, username : str) :
# 	if username in db :
# 		user_data = db[username]
# 		return Customer(user_data)
# 		# return UserInDB(**user_data)

# def authenticate_user(db, username : str, password : str) :
# 	user = get_user(db, username)
# 	if not user :
# 		return False
# 	if not verify_password(password, user.hashed_password) :
# 		return False
# 	return user

# def creat_access_token(data : dict, expires_delta : timedelta or None = None) :
# 	encode = data.copy()
# 	if expires_delta != None :
# 		expires = datetime.utcnow() + expires_delta
# 	else :
# 		expires = datetime.utcnow() + timedelta(minutes=5)
# 	encode.update({"exp" : expires})
# 	encode_jwt = jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)
# 	return encode_jwt

# async def get_current_user(token : str = Depends(OAUTH2_SCHEME)) :
# 	credential_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate your credentials", headers={"WWW-Authenticate" : "Bearer"})
# 	try :
# 		payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
# 		username : str = payload.get("sub")
# 		if username is None :
# 			raise credential_exception
# 		token_data = TokenData(email = username)
# 	except JWTError :
# 		raise credential_exception
# 	user = get_user(db, username= token_data.email)
# 	if user is None :
# 		raise credential_exception
# 	return user

# async def get_current_active_user(current_user : UserInDB = Depends(get_current_user)) :
# 	if current_user.disabled :
# 		raise HTTPException(status_code=400, detail="Inactive User")
# 	return current_user

# @app.post("/token", response_model=Token)
# async def login(form_data : OAuth2PasswordRequestForm = Depends()) :
# 	user = authenticate_user(db, form_data.username, form_data.password)
# 	if not user :
# 		raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect Username or Password", headers={"WWW-Authenticate" : "Bearer"})
# 	access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTE)
# 	access_token = creat_access_token(data={"sub" : user.email}, expires_delta=access_token_expires)
# 	return {"access_token" : access_token, "token_type" : "bearer"}

def	InstanceFinder(classType, attribute, Target) :
    # return (obj for obj in gc.get_objects() if isinstance(obj, classType) and getattr(obj, attribute) == Target)
	for obj in gc.get_objects() :
		if isinstance(obj, classType) and getattr(obj, attribute) == Target :
			return (obj)
	return (None);


# print(get_password_hash("Lament"))
# print(get_password_hash("Bruh"))
# print(get_password_hash("Why"))
