
# rtv_dataeng

A Django-based data dashboard and survey analytics application.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Folder Structure](#folder-structure)
- [Requirements](#requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Project](#running-the-project)
- [Loading Data](#loading-data)
- [Usage](#usage)
- [Testing](#testing)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

---

## Project Overview

This project provides a web dashboard to analyze survey data, particularly poverty and income metrics. It processes CSV data, persists it to a database, and visualizes analytics using Plotly Dash embedded in Django templates.

---

## Features

- Load and clean CSV survey data
- Store survey and household info in a PostgreSQL database (or other supported DB)
- Generate summary statistics and visualizations
- Embed interactive Plotly Dash dashboards in Django views
- Responsive web UI with Bootstrap or custom CSS (adjust as needed)

---

## Folder Structure

rtv_dataeng/
│
├── core/ # Django app for models and business logic
│ ├── migrations/
│ ├── models.py
│ ├── views.py
│ └── ...
├── dashboards/ # Dashboard app with views and templates
│ ├── templates/dashboards/
│ │ ├── dashboard_embed.html
│ ├── views.py
│ └── ...
├── combined_data/ # CSV data files (01_baseline.csv, etc.)
├── rtv_dataeng/ # Django project config folder
│ ├── settings.py
│ ├── urls.py
│ └── ...
├── manage.py # Django management script
├── requirements.txt # Python dependencies
└── README.md # This file

yaml
Copy
Edit

---

## Requirements

- Python 3.8+
- Django 4.x
- pandas
- plotly
- django-plotly-dash (if using Dash integration)
- PostgreSQL (recommended) or any Django-supported DB

---

## Installation

1. Clone this repo:

   ```bash
   git clone git@github.com:mandelashaban593/rtv_dataeng.git
   cd rtv_dataeng
Create a virtual environment and activate it:

bash
Copy
Edit
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
Install Python dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Configure your database in rtv_dataeng/settings.py.

Apply migrations:

bash
Copy
Edit
python manage.py migrate
(Optional) Create a superuser for admin access:

bash
Copy
Edit
python manage.py createsuperuser
Configuration
Place your CSV survey files in the combined_data/ directory:

01_baseline.csv

02_year_one.csv

03_year_two.csv

Update database credentials and other settings in settings.py.

Running the Project
Start the Django development server:

bash
Copy
Edit
python manage.py runserver
Open your browser and visit: http://127.0.0.1:8000/dashboard/

Loading Data
The dashboard view automatically loads and processes CSV files on each request, persisting the cleaned data into the database.

If you want to manually load data or automate it, consider creating a management command.

Usage
View survey summary tables

Interact with embedded Plotly Dash dashboards

Extend with your own charts or data filters in Django views or Dash apps

Testing
Add your tests under the tests/ directory or inside each app.

Run tests with:

bash
Copy
Edit
python manage.py test
Deployment
Configure allowed hosts and debug flags in settings.py.

Use production-ready web servers like Gunicorn or uWSGI.

Serve static files with WhiteNoise or through a CDN.

Secure your database credentials.

Consider containerizing with Docker for consistency.

Contributing
Fork this repository.

Create your feature branch (git checkout -b feature-name).

Commit your changes (git commit -m 'Add some feature').

Push to the branch (git push origin feature-name).

Open a Pull Request.

License
This project is licensed under the MIT License.

Made with ❤️ by Mandela Shaban

yaml
Copy
Edit

---

If you want, I can also help you generate the exact `requirements.txt` or add more detailed setup inst


PROJECT STRUCTURE

rtv_data_engineer_assessment/
├── combined_data/               # Provided CSV and HTML data
│
├── etl/
│   ├── transformations.py       # Cleaning & normalization functions
│   └── schema_mapping.json      # Tracks variable evolution
│
├── rtv_project/
│   ├── manage.py
│   ├── settings.py
│   ├── urls.py                  # Routes including dash apps
│   ├── models.py                # Household, Survey models
│   │
│   ├── ingestion/
│   │   └── import_data.py       # Custom ETL logic
│   │
│   ├── analysis/
│   │   └── metrics.py           # Derived metrics & KPIs
│   │
│   ├── dashboards/
│   │   ├── dash_apps.py         # Dash app definitions
│   │   └── templates/
│   │       └── dashboards/
│   │           └── dashboard_embed.html   # Template for embedded Dash
│   │
│   ├── templates/
│   │   └── home.html            # Simple homepage or login
│   │
│   └── static/                  # JS/CSS for custom styling
│
├── tests/
│   └── test_transformations.py  # Unit tests
│
├── requirements.txt
├── README.md
└── docs/
    ├── architecture_diagram.png
    ├── data_model.md
    └── dashboard_guide.md
