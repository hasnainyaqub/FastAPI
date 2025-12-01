from fastapi import FastAPI
import main

app = FastAPI()

def data_loader():
    with open('patients.json', 'r') as file:
        import json
        data = json.load(file)
    return data

@app.get("/")
def read_root():
    return {"message": "Patient Managment System API"}

@app.get('/about')
def about():
    return {"message": "A fully functional API to manage your patient records."}

@app.get('/view')
def view():
    data = data_loader()
    return data


@app.get('/view/{patient_id}')
def view_patient(patient_id: str):
    data = data_loader()
  
    if patient_id in data:
        
    
        return data[patient_id]
    return {"message": "Patient not found"}