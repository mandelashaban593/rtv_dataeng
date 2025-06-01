A Django-based data dashboard and survey analytics application for visualizing household survey data such as poverty and income metrics.

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

## Project Overview
This project offers a web-based dashboard to analyze survey datasets. It reads and cleans CSV files, stores the information in a PostgreSQL database, and presents analytical insights via interactive Plotly Dash dashboards embedded within Django views.

## Features
Load and clean structured CSV survey files

Store household and survey data in a PostgreSQL (or supported) database

Generate summary statistics and visualizations

Embed Plotly Dash apps within Django templates

Responsive UI using Bootstrap or custom CSS

## Folder Structure

# Project Structure: `rtv_dataeng/`

```plaintext
rtv_dataeng/
│
├── core/                  # Main Django app: models, views, logic
│   ├── migrations/
│   ├── models.py
│   ├── views.py
│   └── ...
│
├── dashboards/            # Dashboard-related views and templates
│   ├── templates/dashboards/
│   │   └── dashboard_embed.html
│   └── views.py
│
├── combined_data/         # Directory for CSV data files
│   └── (e.g., 01_baseline.csv, 02_year_one.csv)
│
├── backend/               # Django project config
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── manage.py              # Django management script
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

## Requirements
Python 3.8+

Django 4.x

pandas

plotly

django-plotly-dash

PostgreSQL (recommended) or other supported database

## Installation
Clone the repository:

git clone git@github.com:mandelashaban593/rtv_dataeng.git
cd rtv_dataeng
Set up a virtual environment:

python -m venv venv

source venv/bin/activate 

 # On Windows: venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt
## Configure your database:

Edit rtv_dataeng/settings.py with your DB credentials.

Apply database migrations:

python manage.py migrate
Create a superuser:

python manage.py createsuperuser
Configuration
Place your CSV survey files in the combined_data/ directory:

01_baseline.csv

02_year_one.csv

03_year_two.csv

Update any custom settings, paths, or credentials in settings.py.

Running the Project
Start the development server:

python manage.py runserver
Visit: http://127.0.0.1:8000/dashboard/

## Loading Data
The dashboard view automatically detects and processes CSV files on each request but you must first login to access it.

Cleaned data is persisted to the database.

For automation or better control, consider writing a Django management command.

## Usage
View summary tables and insights from survey data.

Interact with embedded Plotly Dash visualizations.

Extend the project with new charts, filters, or advanced analytics.

## Testing
Write your tests in a tests/ directory or inside respective Django apps.

Run tests with:

python manage.py test
Deployment
Set DEBUG = False and configure ALLOWED_HOSTS in settings.py.

Use production servers like Gunicorn or uWSGI.

Serve static files with WhiteNoise or via CDN.

Protect sensitive credentials (e.g., use environment variables).

Consider Docker for containerized deployment.

## Contributing
Fork this repository.

Create your feature branch:

git checkout -b feature-name
Commit your changes:

git commit -m "Add some feature"
Push to the branch:

git push origin feature-name
Open a Pull Request.

## License
This project is licensed under the MIT License.

Made with ❤️ by Mandela Shaban

Email: mandelashaban593@gmail.com

Phone: +256763281654

Twitter: mandelashaban51

Instagram:edoctorug1