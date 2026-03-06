from typing import Annotated, Literal, Optional
from pydantic import BaseModel, Field, computed_field

class Patient(BaseModel):
    id: Annotated[str,Field(..., description='ID of the patient', examples=['P001'])]
    name: Annotated[str,Field(..., description='Name of the patient')]
    city: Annotated[str,Field(..., description='City where the patient is living')]
    age: Annotated[int, Field(..., gt = 0, lt=120, description='Age of the patient')]
    gender: Annotated[Literal['male', 'female', 'others'], Field(..., description='Gender of the patient')]
    height: Annotated[float, Field(..., gt=0, description='height of the patient in mtrs')]
    weight: Annotated[float, Field(..., gt=0, description='weight if the patient in kgs')]

    @computed_field
    @property
    def bmi(self)-> float:
        bmi = round(self.weight/(self.height**2), 2)
        return bmi
    
    @computed_field
    @property
    def verdict(self)-> str:
        if self.bmi < 18.5:
            return 'Underweight'
        elif self.bmi < 25:
            return 'Normal'
        elif self.bmi < 30:
            return 'Normal'
        else:
            return 'Obese'
        
class PatientUpdate(BaseModel):
    name: Annotated[Optional[str],Field(..., description='Name of the patient')]
    city: Annotated[Optional[str],Field(..., description='City where the patient is living')]
    age: Annotated[Optional[int], Field(..., gt = 0, lt=120, description='Age of the patient')]
    gender: Annotated[Optional[Literal['male', 'female']], Field(..., description='Gender of the patient')]
    height: Annotated[Optional[float], Field(..., gt=0, description='height of the patient in mtrs')]
    weight: Annotated[Optional[float], Field(..., gt=0, description='weight if the patient in kgs')]


