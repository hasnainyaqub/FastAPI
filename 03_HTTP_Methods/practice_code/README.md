# 03_fastapi - Patient Management System

## Overview

This project demonstrates a Patient Management System using FastAPI with
HTML/CSS frontend integration.\
It covers:

-   FastAPI endpoints for JSON and HTML\
-   Serving HTML templates with Jinja2\
-   Using CSS for clean, modern UI\
-   Rendering patient data dynamically from patients.json

## Features

-   FastAPI backend serving both API and HTML pages\
-   HTML pages: Home, About, Patients\
-   CSS styling for modern design and responsive layout\
-   Dynamic patient table using JavaScript fetch from /patients
    endpoint\
-   Navigation links for easy page switching\
-   Handles patient data stored in JSON format

## Project Structure

    03_fastapi/
    │
    ├── main.py
    ├── patients.json
    ├── templates/
    │   ├── index.html
    │   ├── about.html
    │   └── patients.html
    └── static/
        ├── style.css
        └── patients.css

## Endpoints

  Method   Endpoint         Description
  -------- ---------------- --------------------------------
  GET      /                Home page (HTML)
  GET      /about           About page (HTML)
  GET      /patients        Returns JSON with all patients
  GET      /patients_page   Patients page (HTML table)

## Patients Data

patients.json stores patient details as key-value pairs, with IDs as
keys:

``` json
{
  "P001": {
    "name": "Ananya Verma",
    "city": "Guwahati",
    "age": 28,
    "gender": "female",
    "height": 1.65,
    "weight": 90.0,
    "bmi": 33.06,
    "verdict": "Obese"
  }
}
```

## HTML Pages

### Home (index.html)

-   Welcome section\
-   Features cards\
-   Navigation links

### About (about.html)

-   Project overview\
-   List of key features

### Patients (patients.html)

-   Table displaying all patients\
-   Dynamic loading from /patients endpoint\
-   Styled with CSS for readability and hover effects

## CSS Styling

-   **style.css** -- layout, navigation, cards, and general page styles\
-   **patients.css** -- table styling with hover effects and responsive
    design

## How It Works

-   FastAPI serves JSON for API endpoints and HTML for pages\
-   HTML templates rendered with Jinja2\
-   CSS styles served via /static\
-   JavaScript fetches patient data from /patients and populates the
    table\
-   Navigation ensures consistent user experience across pages
