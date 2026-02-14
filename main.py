from fastapi import FastAPI

app = FastAPI() # Create a FastAPI instance

@app.get("/") # Define a GET endpoint at the root URL (Decorator))
def hello(): # This function will be called when a GET request is made to the root URL
    return {"message": "Hello World!!!"}

@app.get("/about") 
def about(): # This function will be called when a GET request is made to the /about URL
    return {"message": "This is a simple FastAPI application."} 