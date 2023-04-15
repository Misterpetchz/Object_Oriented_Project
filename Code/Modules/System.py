from Modules.settings import *
from Modules.UserAccount import *

class System :
    def __init__(self) :
        self.User_DB = []

    def verify_password(plain_password, hashed_password) :
        return PWD_CONTEXT.verify(plain_password, hashed_password)

    def get_password_hash(self, password) :
        return PWD_CONTEXT.hash(password)

    def get_user(self, username : str) :
        for i in self.User_DB :
            if i._email == username :
                return i
		# user = InstanceFinder(Customer, "_email", username)
        # if not user == None :
        #     return user
        # if username in db :
        # 	user_data = db[username]
        # 	return Customer(user_data)
            # return UserInDB(**user_data)

    def authenticate_user(self, username : str, password : str) :
        user = self.get_user(username)
        if not user :
            return False
        if not System.verify_password(password, user._password) :
            return False
        return user

    def creat_access_token(self, data : dict, expires_delta : timedelta or None = None) :
        encode = data.copy()
        if expires_delta != None :
            expires = datetime.utcnow() + expires_delta
        else :
            expires = datetime.utcnow() + timedelta(minutes=5)
        encode.update({"exp" : expires})
        encode_jwt = jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)
        return encode_jwt

    def register(self, customer):
        self.User_DB.append(customer)


    async def get_current_user(self, token : str = Depends(OAUTH2_SCHEME)) :
        credential_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate your credentials", headers={"WWW-Authenticate" : "Bearer"})
        try :
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            username : str = payload.get("sub")
            if username is None :
                raise credential_exception
            token_data = TokenData(email = username)
        except JWTError :
            raise credential_exception
        user = self.get_user(username= token_data.email)
        if user is None :
            raise credential_exception
        return user