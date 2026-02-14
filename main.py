from fastapi import FastAPI
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