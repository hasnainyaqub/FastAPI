from fastapi import FastAPI, Path, HTTPException

app = FastAPI()

def data_loader():
    with open('patients.json', 'r') as file:
        import json
        data = json.load(file)
    return data

@app.get('/')
def home():
    return {'message': 'Welcome to the Patient Management System API'}

@app.get('/about')
def about():
    return {'message': 'A fully functional API to manage your patient records'}

@app.get('/view')
def view():
    data = data_loader()
    return data
    
@app.get('/patient/{patient_id}')
def view_patient(patient_id: str = Path(..., description='ID of the patient in the DB', example='P001')):
    data = data_loader()
    
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail='Patient not found')