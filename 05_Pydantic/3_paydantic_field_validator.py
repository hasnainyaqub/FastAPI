from pydantic import BaseModel, EmailStr, Field, field_validator
from typing import List, Dict, Annotated

# Base Model
class user(BaseModel):
    name: Annotated[str, Field(...,min_length=3, max_length=50)]
    email: EmailStr
    age: Annotated[int, Field(..., ge=18, le=80)]
    
# field Validator
    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        valid_dimains = ["edu.com"]
        # abc@gmail.com
        domain_name = value.split('@')[-1]

        if domain_name not in valid_dimains: raise ValueError('Not a valid domain') 
        return value
    
    @field_validator('name')
    @classmethod
    def transform_name(cls, value):
        return value.upper()

# User Data Function
def user_data(user):
    name = user.name
    user.email
    user.age
    print(name)
    


user_name = str(input('Enter your name: '))
# user_email = str(input('Enter your Email:'))
user_age = int(input('Enter your age:'))

data = user(name=user_name, email='hasnain@edu.com', age=user_age)

print(user_data(data))
