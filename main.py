from fastapi import FastAPI, Path, HTTPException, Query
import json

app = FastAPI() # Create a FastAPI instance

def load_data():
    # This function will load patient data from a file or database
    # For now, we will just return an empty list
    with open("patients.json", "r") as f:
        data = json.load(f)
    return data

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