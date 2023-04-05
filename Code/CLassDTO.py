from pydantic import BaseModel
class AddBookDTO(BaseModel):
    name:str
    confirm:bool
    password:str