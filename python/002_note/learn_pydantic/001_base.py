from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, ValidationError, validator, Field

from pydantic import BaseModel, Field


class User(BaseModel):
    id: int
    # id: Field(int, field_name='error -- msg')
    name = 'John Doe'
    signup_ts: Optional[datetime] = None
    friends: List[int] = []
    # a: Field(regex='12')

    # class Config:
    #     min_anystr_length = 6  # 令Password类中所有的字符串长度均要不少于6
    #     max_anystr_length = 20  # 令Password类中所有的字符串长度均要不大于20


external_data = {
    'id': '111',
    'signup_ts': '2019-06-01 12:22',
    'friends': [1, 2, '3'],

}
user = User(**external_data)

# try:
#     User(signup_ts='broken', friends=[1, 2, 'not number'])
# except ValidationError as e:
#     print(e.json())
