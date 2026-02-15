# Better organisation
# Reusability
# Readaptability
# Validation

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

address_dict = {"city": "Hyd", "state": "ts", "pin": "504251"}

address1 = Address(**address_dict)

patient_dict =  {"name": "Neha Sinha", "gender": "male", "age": 30, "address": address1}

patient1 = Patient(**patient_dict) # ** is for unpacking the dictionary

# temp = patient1.model_dump() # converts to dictionary
# temp = patient1.model_dump(include=["name", "gender"])
temp = patient1.model_dump(exclude=["name", "gender"])
temp_json = patient1.model_dump_json() # converts to json


print(temp)
# print(type(temp_json))

# print(patient1)
# print(patient1.name)
# print(patient1.address.city)