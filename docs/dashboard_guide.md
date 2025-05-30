Dashboard Guide
Overview
This guide explains how to use, customize, and extend the interactive dashboard integrated into the Django application using django-plotly-dash. The dashboard provides visual insights into poverty metrics and related data analytics based on household surveys.

Contents
    Accessing the Dashboard

    Dashboard Features

    Extending Dash Apps

    Embedding Dashboards

    Authentication & Permissions

    Troubleshooting

Accessing the Dashboard
Start the Django development server:

python manage.py runserver
Open your browser and navigate to:

http://localhost:8000/dashboard/
Login using your credentials (if authentication is enabled).
Upon login, you will be redirected to the dashboard page.

Dashboard Features
Interactive Graphs:
Visualize poverty metrics such as income distribution, education levels, access to utilities, etc.
Charts are created using Plotly and embedded into Django templates.

Filtering & Controls:
Users can filter data by region, survey year, household size, and other variables to dynamically update charts.

Real-time Updates:
Dashboard components respond to user inputs without reloading the page.

Responsive Layout:
Works well on different screen sizes, including tablets and desktops.

Extending Dash Apps
All Dash applications are defined in rtv_project/dashboards/dash_apps.py.

Adding a New Dash App
Define a new Dash app instance inside dash_apps.py:

from django_plotly_dash import DjangoDash
import dash_core_components as dcc
import dash_html_components as html

new_dash_app = DjangoDash('NewDashApp')

new_dash_app.layout = html.Div([
    dcc.Graph(id='new-graph', figure={
        'data': [{'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar'}],
        'layout': {'title': 'Sample Bar Chart'}
    })
])
Include the Dash app route in your Django urls.py via django_plotly_dash.urls.

Update or create Django templates to embed this new app.

Embedding Dashboards in Django Templates
Dashboards are embedded in Django templates using the {% plotly_app %} template tag.

Example (located in rtv_project/dashboards/templates/dashboards/dashboard_embed.html):
{% load plotly_dash %}
<!DOCTYPE html>
<html>
<head>
    <title>Dashboard</title>
</head>
<body>
    <h1>Poverty Metrics Dashboard</h1>
    {% plotly_app name="PovertyDashboard" %}
</body>
</html>
Render this template via a Django view to display the dashboard in your website.

Authentication & Permissions
You can protect the dashboard route with Django’s built-in authentication decorators.

Example in dashboards/views.py:


from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def dashboard_view(request):
    return render(request, 'dashboards/dashboard_embed.html')
Ensure users must log in before accessing the dashboard.

Troubleshooting
ModuleNotFoundError: No module named 'dpd_static_support'
Make sure you have installed django-plotly-dash and included 'dpd_static_support' in INSTALLED_APPS.

Static files not loading
Run python manage.py collectstatic and verify your static files configuration.

Dash callbacks not updating
Ensure your Dash app callbacks are properly defined and no exceptions are raised during execution.

Additional Resources
django-plotly-dash Documentation

Plotly Dash Documentation

Django Official Documentation

End of Dashboard Guide