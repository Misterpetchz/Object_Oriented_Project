	#? External Lib
from Modules.settings import *
from Modules.UserAccount import UserAccount, Customer

app = FastAPI()

User_DB = []
# db = {
# 	"Medkit101@gmail.com" : {
# 		"email" : "Medkit101@gmail.com",
# 		"full_name" : "Dante Durante",
# 		"gender" : "Unknown",
# 		"tel" : "101564",
# 		"address" : "District 7",
# 		"email_noti" : True,
# 		"sms_noti" : True,
# 		"disabled" : False,
# 		"hashed_password" : "$2b$12$71C2.b9fJlp.3903g3klI.m8aIC4hRyurIX8ANpqoyWfA9QIAQ/82"
# 	},
# 	"Test101@gmail.com" : {
# 		"email" : "Test101@gmail.com",
# 		"full_name" : "Dante Durante",
# 		"gender" : "Unknown",
# 		"tel" : "101564",
# 		"address" : "District 7",
# 		"email_noti" : True,
# 		"sms_noti" : True,
# 		"disabled" : False,
# 		"hashed_password" : "$2b$12$b4rMellphLAUtntHySUkbexQ/IqSNba1KDEATosuU/lOKpBofIb8G"
# 	},
# 	"Test202@gmail.com" : {
# 		"email" : "Test202@gmail.com",
# 		"full_name" : "Dante Durante",
# 		"gender" : "Unknown",
# 		"tel" : "101564",
# 		"address" : "District 7",
# 		"email_noti" : True,
# 		"sms_noti" : True,
# 		"disabled" : False,
# 		"hashed_password" : "$2b$12$AqhPzCx2ELR29n5iVVsiSuz94XDAX.hkjQf6f4KoEjYYAXLJj/85W"
# 	},
# }

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

async def get_current_active_user(current_user : Customer = Depends(Customer.get_current_user)) :
	# print(current_user.__dict__)
	if current_user._disabled :
		raise HTTPException(status_code=400, detail="Inactive User")
	return current_user

@app.put("/users/edit")
async def info_verification(email : Optional[str] = None, password : Optional[str] = None, full_name : Optional[str] = None, gender : Optional[str] = None, tel : Optional[str] = None, address : Optional[str] = None,
				email_noti : Optional[bool] = None, sms_noti : Optional[bool] = None, id : Customer = Depends(Customer.get_current_user)) :
	if (id == None) :
		return {"Error-101" : "Didn't find any account with this id"}
	id._email = email or id._email
	id._password = password or id._password
	id._full_name = full_name or id._full_name
	id._gender = gender or id._gender
	id._tel = tel or id._tel
	id._address = address or id._address
	# id._email_notification = email_noti if email_noti != None else id._email_notification
	# id._sms_notification = sms_noti if sms_noti != None else id._sms_notification
	if email_noti != None :
		id.email_notification = email_noti
	if email_noti != None :
		id.sms_notification = sms_noti

@app.put("/users/registration")
async def registration(email : str , password : str, full_name : str, gender : str, tel : str, address : str,
				email_noti : bool, sms_noti : bool) :
	input_dict = {}
	input_dict['_email'] = email
	input_dict['_password'] = Customer.get_password_hash(password)
	input_dict['_full_name'] = full_name
	input_dict['_gender'] = gender
	input_dict['_tel'] = tel
	input_dict['_address'] = address
	input_dict['__email_notification'] = email_noti
	input_dict['__sms_notification'] = sms_noti

	User_DB.append(Customer(input_dict))

@app.post("/token", response_model=Token)
async def login(form_data : OAuth2PasswordRequestForm = Depends()) :
	user = Customer.authenticate_user(form_data.username, form_data.password)
	if not user :
		raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect Username or Password", headers={"WWW-Authenticate" : "Bearer"})
	access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTE)
	access_token = Customer.creat_access_token(data={"sub" : user._email}, expires_delta=access_token_expires)
	return {"access_token" : access_token, "token_type" : "bearer"}

@app.get("/users/me")
async def view_info(userid : Customer = Depends(get_current_active_user)):
	# id = InstanceFinder(Customer, "_email", userid)
	# if (id == None) :
	# 	return {"Error-101" : "Didn't find any account with this id"}
	# else :
		return (userid)

# print(get_password_hash("Lament"))
# print(get_password_hash("Bruh"))
# print(get_password_hash("Why"))
