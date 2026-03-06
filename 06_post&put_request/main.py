from fastapi import FastAPI, Path, HTTPException, Query
from fastapi.responses import JSONResponse
from config import Patient, PatientUpdate
from data import data_loader, save_data

app = FastAPI()

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
def sort_patients(sort_by: str = Query(..., description='Sort on the basis of height, weight or bmi', examples='height'), order: str = Query(..., description='Sort in ascending or descending order', examples='asc')):

    valid_fields = ['height', 'weight', 'bmi']

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail='Invalid sort field')
    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail='Invalid order')

    data = data_loader()
    sort_order = True if order == 'desc' else False
    sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by, 0), reverse=sort_order)
    return sorted_data

@app.post('/create')
def create_patient(patient: Patient):
    # load existing data
    data = data_loader()

    # check if the patient already exists
    if patient.id in data:
        raise HTTPException(status_code=400, detail='Patient already exists')
    

    # new patient add to the database
    data[patient.id] = patient.model_dump(exclude=['id'])

    #save into the json file 
    save_data(data)

    return JSONResponse(status_code=201, content={'message': 'Patient created successfully'})

@app.put('/edit/{patient_id}')
def update_patient(patient_id: str, patient_update: PatientUpdate):

    data = data_loader()

    if patient_id not in data:
        raise HTTPException(status_code=400, detail='patient not found')
    
    existing_patient_info = data[patient_id]
    updated_patient_info = patient_update.model_dump(exclude_unset=True)

    for key, value in updated_patient_info.items():
        existing_patient_info[key] = value

    existing_patient_info['id'] = patient_id
    patient_pydantic_object = Patient(**existing_patient_info)

    # pydantic object -> dict
    existing_patient_info = patient_pydantic_object.model_dump(exclude='id')

    data[patient_id] = existing_patient_info

    # save data
    save_data(data)

    return JSONResponse(status_code=200, content={'message': 'Patient updated'})

@app.delete('/delete/{patient_id}')
def delete_patient(patient_id:str):
    data = data_loader()

    if patient_id not in data:
        raise HTTPException(status_code=400, detail='Patient not found')
    
    del data[patient_id]

    save_data(data)

    return JSONResponse(status_code=200, content={'message': 'Patient deleted'})
