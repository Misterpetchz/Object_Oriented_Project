from pydantic import BaseModel
class AddBooktoBasketDTO(BaseModel):
    name:str
    confirm:bool
    password:str

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
    rating:str
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
    test:str
    
class RemoveBookDTO(BaseModel):
    index:int
    book_name:str

class SearchBookDTO(BaseModel):
    string:str
    
class AddRatingDTO(BaseModel):
    comment:str
    score:int