from pydantic import BaseModel
from datetime import datetime

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
        
class BookModel(BaseModel):
        cover = str
        brief = str
        creator = str
        name = str
        book_info = str
        book_publisher = str
        book_preview = str
        critic_review = str
        table_of_content = str
        summary = str
        genre = str
        date_created = str
        price = int
        amount_in_stock = int
