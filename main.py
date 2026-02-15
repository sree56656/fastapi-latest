from fastapi import FastAPI, Path, HTTPException, Query
from fastapi.responses import JSONResponse
import json
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal, Optional

app = FastAPI() # Create a FastAPI instance

class Patient(BaseModel):
    id: Annotated[str, Field(..., description="ID of the patient", examples=["P001"])]
    name: Annotated[str, Field(..., description="NAME of the patient", examples=["Josh"])]
    city: Annotated[str, Field(..., description="NAME of the patient", examples=["Josh"])]
    age: Annotated[int, Field(..., gt=0, lt=120, description="age of the patient", examples=["Josh"])]
    gender: Annotated[Literal['male', 'female', 'others'], Field(..., description="gender of the patient", examples=["male"])]
    height: Annotated[float, Field(..., gt=0, description="height of the patient in mtrs")]
    weight: Annotated[float, Field(..., gt=0, description="weight of the patient in kgs")]
    
    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi
    
    @computed_field
    @property
    def verdict(self) -> str:
        if self.bmi < 18.5:
            return 'under weight'

        elif self.bmi < 25:
            return 'Normal'
        
        elif self.bmi < 30:
            return 'Normal'
        
        else:
            return 'Obese'

class PatientUpdate(BaseModel):
    name: Annotated[Optional[str], Field(default=None)]
    city: Annotated[Optional[str], Field(default=None)]
    age: Annotated[Optional[int], Field(default=None, gt=0)]
    gender: Annotated[Optional[Literal['male', 'female']], Field(default=None)]
    height: Annotated[Optional[float], Field(default=None, gt=0)]
    weight: Annotated[Optional[float], Field(default=None, gt=0)]


def load_data():
    # This function will load patient data from a file or database
    # For now, we will just return an empty list
    with open("patients.json", "r") as f:
        data = json.load(f)
    return data

def save_data(data):
    with open("patients.json", 'w') as f:
        json.dump(data, f)

@app.get("/") # Define a GET endpoint at the root URL (Decorator))
def hello(): # This function will be called when a GET request is made to the root URL
    return {"message": "Patient management system API"} # Return a JSON response with a message

@app.get("/about") 
def about(): # This function will be called when a GET request is made to the /about URL
    return {"message": "A fully functional API to manage your patient records"}
 # Return a JSON response with a message

@app.get("/view")
def view_patients():
    data = load_data() # Load patient data
    return {"patients": data} # Return a JSON response with the patient data 

# path parameter to get a specific patient by ID
@app.get("/patient/{patient_id}")
def get_patient(patient_id: str = Path(..., description="The ID of the patient in the DB")): # Define a path parameter for the patient ID
    data = load_data()
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail="Patient not found")

@app.post("/sort")
def sort_patients(sort_by: str = Query(..., description="The field to sort by height, weight, bmi"), order: str = Query("asc", description="The order to sort by asc or desc")): # Define a query parameter for sorting
    valid_fields = ["height", "weight", "bmi"]
    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f"Invalid sort field. Valid fields are: {', '.join(valid_fields)}")
    
    if order not in ["asc", "desc"]:
        raise HTTPException(status_code=400, detail="Invalid sort order. Valid orders are: asc, desc")
    
    data = load_data()
    sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by, 0), reverse=(order == "desc"))
    return {"sorted_patients": sorted_data}

@app.post('/create')
def create_patient(patient: Patient):  # Patient is a data type of class
    
    # load existing data in dictionary format
    data = load_data() 

    # check if patient is already exists
    if patient.id in data:
        raise HTTPException(status_code=400, detail="patient already exists")
    
    # new patient to add to database
    data[patient.id] = patient.model_dump(exclude=['id'])  # dictionary

    # save data
    save_data(data)
    return JSONResponse(status_code=201, content={'message': 'patient created successfully'})


@app.put('/edit/{patient_id}')
def update_patient(patient_id: str, patient_update: PatientUpdate):

    data = load_data()

    if patient_id not in data:
        raise HTTPException(status_code=404, detail='Patient not found')
    
    existing_patient_info = data[patient_id]

    updated_patient_info = patient_update.model_dump(exclude_unset=True)

    for key, value in updated_patient_info.items():
        existing_patient_info[key] = value

    #existing_patient_info -> pydantic object -> updated bmi + verdict
    existing_patient_info['id'] = patient_id
    patient_pydandic_obj = Patient(**existing_patient_info)
    #-> pydantic object -> dict
    existing_patient_info = patient_pydandic_obj.model_dump(exclude='id')

    # add this dict to data
    data[patient_id] = existing_patient_info

    # save data
    save_data(data)

    return JSONResponse(status_code=200, content={'message':'patient updated'})

@app.delete('/delete/{patient_id}')
def delete_patient(patient_id: str):

    data = load_data()

    if patient_id not in data:
        raise HTTPException(status_code=404, detail='patient is not available')
    
    del data[patient_id]
    save_data(data)

    return JSONResponse(status_code=200, content={'Patient deleted'})

