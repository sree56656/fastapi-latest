# If age > 60 they should provide emergency ph number

from pydantic import BaseModel, EmailStr, computed_field
from typing import List, Dict, Optional, Annotated

# Field --> used to attach metadata and condition for variable

class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight: float
    height: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    @computed_field
    @property
    def calculated_bmi(self) -> float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi

    
def insert_patient(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print("BMI: ", patient.calculated_bmi)
    print("Inserted patient into database")

patient_info = {"name": "John Doe", "email": "rsreekanth@hdfc.com", "age": "110", "weight": "75.2", "height": "1.72", "married": "true",  "allergies": ["pollen", "dust"],"contact_details": {"email": "john.doe@example.com", "emergency": "123-456-7890"}}

patient1 = Patient(**patient_info)
insert_patient(patient1)