from pydantic import BaseModel

class Address(BaseModel):
    city: str
    state: str
    pin: str

class Patient(BaseModel):
    name: str
    gender: str
    age: int
    address: Address

address_dict = {'city': 'xyz', 'state': 'abc', 'pin': '1A3BD82'}

address1 = Address(**address_dict)

data = Patient(name='Hasnain Yaqoob', gender='male', age=17, address=address1)

print(data)