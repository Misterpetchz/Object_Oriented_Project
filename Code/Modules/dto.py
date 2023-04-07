from pydantic import BaseModel
from datetime import datetime

class CreditCardDTO(BaseModel):
    card_num : str
    expire_date : str
    cvc : str

class ModifyBranchDTO(BaseModel):
    branch_name : str
    open_time : str
    location : str
    tel : str
    line_id : str
    facebook_id : str
    add_book : list
    remove_book : list

class AddBranchDTO(BaseModel):
    branch_name : str
    open_time : str
    location : str
    tel : str
    line_id : str
    facebook_id : str

class EventDTO(BaseModel):
    event_name : str
    event_start : str
    event_end : str
    discounted_percentage : int

class ModifyEventDTO(BaseModel):
    event_name : str
    event_start : str
    event_end : str
    discounted_percentage : int

class QrCodeDTO(BaseModel):
    amount : int
    date : str