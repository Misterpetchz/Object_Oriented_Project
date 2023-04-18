from pydantic import BaseModel
from datetime import datetime
class AddBooktoBasketDTO(BaseModel):
    amount:int

class AddBookDTO(BaseModel):
    cover:str
    brief:str
    creator:str
    name:str
    book_info:str
    book_publisher:str
    book_preview:str
    critic_review:str
    table_of_content:str
    summary:str
    genre:list[str]
    date_created:str
    price:int
    amount:int
    
class AddBranchDTO(BaseModel):
    branch_name:str
    open_time:str
    location:str
    tel:str
    line_id:str
    facebook_id:str
    
class MakeOrderDto(BaseModel):
    status : bool
    
    
class RemoveBookDTO(BaseModel):
    index:int
    book_name:str

class SearchBookDTO(BaseModel):
    string:str
    
class AddRatingDTO(BaseModel):
    comment:str
    score:int
    
class Branchs(BaseModel):
    branch_name : str
    open_time : str
    location : str
    tel : str
    line_id : str
    facebook_id : str

class ModifyBookDTO(BaseModel):
    cover:str|None
    brief:str|None
    creator:str|None
    name:str|None
    book_info:str|None
    book_publisher:str|None
    book_preview:str|None
    critic_review:str|None
    table_of_content:str|None
    summary:str|None
    genre:list[str]|None
    date_created:str|None
    rating:str|None
    price:int|None
    amount:int|None

class CreditCards(BaseModel):
    card_num : str
    expire_date : datetime
    cvc : str


class BranchModel(BaseModel):
        branch_name = str
        open_time = str
        location = str
        tel = str
        line_id = str
        facebook_id = str
        product_in_stock = str
    
    
class RegisterDTO(BaseModel):
    email : str 
    password : str
    full_name : str
    gender : str
    tel : str
    address : str
    email_noti : str
    sms_noti : str