from fastapi import FastAPI, Path, HTTPException, Query

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
def view_patient(patient_id: str = Path(..., description='ID of the patient in the DB', examples='P001')):
    data = data_loader()
    
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail='Patient not found')

@app.get('/sort')
def sort_patients(sort_by: str = Query(..., description='Sort on the basis of height, weight or bmi', example='height'), order: str = Query(..., description='Sort in ascending or descending order', examples='asc')):

    valid_fields = ['height', 'weight', 'bmi']

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail='Invalid sort field')
    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail='Invalid order')

    data = data_loader()
    sort_order = True if order == 'desc' else False
    sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by, 0), reverse=sort_order)
    return sorted_data
