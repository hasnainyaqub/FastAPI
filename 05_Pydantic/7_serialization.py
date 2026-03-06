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

temp = data.model_dump()
temp_json = data.model_dump_json(include=['name', 'age'])

print('--'*20)
print(temp)
print(type(temp))
print('--'*20)
print(temp_json)
print(type(temp_json))
print('--'*20)