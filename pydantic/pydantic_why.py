from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

# Pydantic allows you to define data models with type validation and parsing of input data. It helps ensure that the data you work with is of the expected type and format, reducing the chances of runtime errors.
# Field --> used to attach metadata and condition for variable

class Patient(BaseModel):
    # name: str = Field(max_length=50)
    name: Annotated[str, Field(max_length=50, title="Name of the patient", description="give the patient name in lessthan 50 chars", examples=["Nitish", "Amit"])] # metadata attachment
    email: EmailStr
    age: int
    weight: float = Field(gt=0, lt=120) # field defines range or condition
    # married: bool = False # Default value for married is False if not provided
    married: Annotated[bool, Field(default=None, description="Is the patient married or not")] # metadata 
    allergies: Annotated[Optional[List[str]], Field(default=None, max_length=5)] # Optional field, can be None if not provided
    contact_details: Dict[str, str]

# By using Pydantic, you can easily create instances of the Patient model from dictionaries or other data sources, and it will automatically validate the input data against the defined types. If the data is invalid, Pydantic will raise a ValidationError, making it easier to catch and handle errors early in the development process.
def insert_patient(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print("Inserted patient into database")

# pydantic can automatically age 30 string to integer
# patient_info = {"name": "John Doe", "age": "30", "weight": "70.5", "married": "true", "allergies": ["pollen", "dust"], "contact_details": {"email": "john.doe@example.com", "phone": "123-456-7890"}}

# verifying optional field allergies, if not provided it will be None
# patient_info = {"name": "John Doe", "age": "30", "weight": "70.5", "married": "true", "contact_details": {"email": "john.doe@example.com", "phone": "123-456-7890"}}

patient_info = {"name": "John Doe", "email": "rsreekanth@gmail.com", "age": "30", "weight": "70.5", "married": "true", "contact_details": {"email": "john.doe@example.com", "phone": "123-456-7890"}}


patient1 = Patient(**patient_info)
insert_patient(patient1)