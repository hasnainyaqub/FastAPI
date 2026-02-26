from pydantic import BaseModel, Field, model_validator
from typing import List, Dict, Annotated

class Patient(BaseModel):
    name : Annotated[str, Field(..., min_length=3, max_length=50)]
    age : int = Field(..., ge=18, le=100)
    contact_details: Dict[str, str]

    # model validator
    @model_validator(mode='after')
    def validate_emergency_contact(cls, model):
        if model.age >= 60 and 'emergency' not in model.contact_details:
            raise ValueError('Patients older than 60 require emergency contact')
        return model

def patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.contact_details)


while True:
    user = input('Enter your name: ')
    age = int(input('Enter your age: '))
    contact_details = input('Enter contact details : ')
    if age >= 60 : 
        user_emergency_contact = input('please enter emergency contact details: ')
        data = Patient(name=user, age=age, contact_details={'home':contact_details, 'emergency': user_emergency_contact})
    else:
        data = Patient(name=user, age=age, contact_details={'home':contact_details})
    patient_update = patient_data(data)

    print(patient_data)

    quit = input('do you want to quit, (yes/no): ')
    if quit.lower()== 'yes':
        break
    else: 
        continue