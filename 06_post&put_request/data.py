import json

def data_loader():
    with open('patients.json', 'r') as file:
        import json
        data = json.load(file)
    return data

def save_data(data):
    with open('patients.json', 'w') as f:
        json.dump(data, f)