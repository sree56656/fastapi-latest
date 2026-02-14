from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
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

    # field_validator is a class method which requires cls and value of the fields which needs validation
    @field_validator("email")
    @classmethod
    def email_validator(cls, value):

        valid_domains = ["hdfc.com", "icici.com"]
        # abc@gmail.com
        domain_name = value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError('Not a valid domain')
        
        return value
    
    # Name making to upper case and mode can be before or after
    @field_validator("name", mode="after")
    @classmethod
    def transform_name(cls, value):
        return value.upper()
    
    # @field_validator("age", mode="before")
    @field_validator("age", mode="after")
    @classmethod
    def validate_age(cls, value):
        if 0 < value < 100:
            return value
        else:
            raise ValueError("Age must be between 0 to 100")

def insert_patient(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print("Inserted patient into database")

# pydantic can automatically age 30 string to integer
# patient_info = {"name": "John Doe", "age": "30", "weight": "70.5", "married": "true", "allergies": ["pollen", "dust"], "contact_details": {"email": "john.doe@example.com", "phone": "123-456-7890"}}
patient_info = {"name": "John Doe", "email": "rsreekanth@hdfc.com", "age": "30", "weight": "70.5", "married": "true",  "allergies": ["pollen", "dust"],"contact_details": {"email": "john.doe@example.com", "phone": "123-456-7890"}}


patient1 = Patient(**patient_info)
insert_patient(patient1)