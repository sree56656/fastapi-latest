# If age > 60 they should provide emergency ph number

from pydantic import BaseModel, EmailStr, model_validator
from typing import List, Dict, Optional, Annotated

# Field --> used to attach metadata and condition for variable

class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    @model_validator(mode = "after")
    def validate_emergency_contact(cls,model):
        if model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError("Patients age > 60 must provide emergency phone number")
        return model

    
def insert_patient(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print("Inserted patient into database")

patient_info = {"name": "John Doe", "email": "rsreekanth@hdfc.com", "age": "110", "weight": "70.5", "married": "true",  "allergies": ["pollen", "dust"],"contact_details": {"email": "john.doe@example.com", "emergency": "123-456-7890"}}

patient1 = Patient(**patient_info)
insert_patient(patient1)