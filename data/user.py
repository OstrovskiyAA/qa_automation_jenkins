import dataclasses

@dataclasses.dataclass
class Users:
    first_name :str
    last_name:str
    email:str
    gender:str
    mobile_number:str
    date_by_your_own_day:int
    date_by_your_own_month:str
    date_by_your_own_year:int
    subject:str
    hobby:str
    name_of_file:str
    address:str
    state:str
    city:str