from Modules.settings import *
from Modules.UserAccount import *
from datetime import datetime


class System:
	def __init__(self):
		self.__User_DB = []

# + Getter / Setter {START}

	@property
	def User_DB(self):
		return self.__User_DB

	@User_DB.setter
	def User_DB(self, new):
		self.User_DB = new

# + Getter / Setter {START}

# Description : Hash password with secret key to get encrypted password
	def verify_password(plain_password, hashed_password):
		return PWD_CONTEXT.verify(plain_password, hashed_password)

# Description : Testing tool, get the password hashed with secret key
	def get_password_hash(self, password):
		return PWD_CONTEXT.hash(password)

# Description : Get user with the same username(email) from the database
	def get_user(self, username: str):
		for i in self.__User_DB:
			if i._email == username:
				return i

# Description : Check if user is exist within database and check the password return user instance
	def authenticate_user(self, username: str, password: str):
		user = self.get_user(username)
		if not user:
			return False
		if not System.verify_password(password, user._password):
			return False
		return user

# Description : Create token for the logged user suppose to use when logging in
	def creat_access_token(self, data: dict, expires_delta: timedelta or None = None):
		encode = data.copy()
		if expires_delta != None:
			expires = datetime.utcnow() + expires_delta
		else:
			expires = datetime.utcnow() + timedelta(minutes=5)
		encode.update({"exp": expires})
		encode_jwt = jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)
		return encode_jwt

# Description : Add user to database
	def register(self, customer):
		self.__User_DB.append(customer)

# Description : Get the current active user instance based on token stored in localstorage
	async def get_current_user(self, token: str = Depends(OAUTH2_SCHEME)):
		credential_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
											 detail="Could not validate your credentials", headers={"WWW-Authenticate": "Bearer"})
		try:
			payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
			username: str = payload.get("sub")
			if username is None:
				raise credential_exception
			token_data = TokenData(email=username)
		except JWTError:
			raise credential_exception
		user = self.get_user(username=token_data.email)
		if user is None:
			raise credential_exception
		return user

# Description : Check the owner of the payment returned user instance
	def find_user_by_payment_id(self, id):
		for user in self.__User_DB:
			if id == user.payment_id:
				return user
