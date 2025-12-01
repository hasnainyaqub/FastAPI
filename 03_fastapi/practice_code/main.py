from fastapi import FastAPI

app = FastAPI()

# create a function to read patients.json file
def read_patients_file():
    import json
    with open('patients.json', 'r') as file:
        return json.load(file)


# Why?
# FastAPI needs Request so the HTML template can access route information.
# Jinja2Templates allows FastAPI to load and render HTML files.
from fastapi import Request
from fastapi.templating import Jinja2Templates

# Create templates folder support
templates = Jinja2Templates(directory="templates")
# You tell FastAPI that all your HTML files are inside the templates folder.
# Without this step, FastAPI cannot find your HTML.
# -------------------------------------------



# Serve static CSS files
from fastapi.staticfiles import StaticFiles
app.mount('/static', StaticFiles(directory='static'), name='static')
# Why?
# Your website also needs CSS files.
# StaticFiles tells FastAPI to serve files like style.css, images, scripts, fonts, and so on.
# ------------------------------------------
# When a browser opens
# /static/style.css
# it gets your CSS file.
# ----------------------------------------------




# Creating page routes for HTML
# Your earlier routes were simple JSON routes.
# Now we convert them to HTML.
# Home route
@app.get('/')
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

''' (
    What and why?
@app.get("/") means when someone visits the home page
We return the HTML file index.html
The dictionary { "request": request } is required by Jinja2
If you forget it, your template will not work.) '''


# About route
@app.get('/about')
def about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})
# Same idea
# It simply loads the about.html page.





@app.get('/patients') 
def get_patients(): 
    patients = read_patients_file() 
    return {"patients": patients}

@app.get("/patients_page")
def patients_page(request: Request):
    return templates.TemplateResponse("patients.html", {"request": request})








