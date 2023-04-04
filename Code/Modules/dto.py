from pydantic import BaseModel
from datetime import datetime

class CreditCards(BaseModel):
    card_num : str
    expire_date : datetime
    cvc : str


class BranchModel(BaseModel):
        branch_name = str
        open_time = datetime
        location = str
        tel = str
        line_id = str
        facebook_id = str
        product_in_stock = str
