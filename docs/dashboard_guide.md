# Dashboard Guide

This guide explains how to use, customize, and extend the interactive dashboard integrated into the Django application using `django-plotly-dash`. The dashboard provides visual insights into poverty metrics and related analytics based on household survey data.

---

## Table of Contents

- [Accessing the Dashboard](#accessing-the-dashboard)
- [Dashboard Features](#dashboard-features)
- [Extending Dash Apps](#extending-dash-apps)
- [Embedding Dashboards in Django Templates](#embedding-dashboards-in-django-templates)
- [Authentication & Permissions](#authentication--permissions)
- [Troubleshooting](#troubleshooting)
- [Additional Resources](#additional-resources)

---

## Accessing the Dashboard

1. Start the Django development server:

   ```bash
   python manage.py runserver

Log in with your credentials (if authentication is enabled).

Upon successful login, you will be redirected to the dashboard page.

## Dashboard Features
Interactive Graphs

Visualize key poverty metrics such as:

Income distribution

Education levels

Access to utilities

Charts are built with Plotly and embedded within Django templates.

Filtering & Controls
Users can filter the dashboard data by:

Region

Survey year

Household size

Other relevant dimensions

Charts update dynamically based on filter selection.

Real-Time Updates
The dashboard responds to user inputs without reloading the page.

Responsive Layout
Designed to work well across screen sizes (desktop, tablet, etc.).

## Extending Dash Apps
All Dash applications are defined inside:


rtv_project/dashboards/dash_apps.py
Adding a New Dash App
Define a new app in dash_apps.py:

from django_plotly_dash import DjangoDash
import dash_core_components as dcc
import dash_html_components as html

new_dash_app = DjangoDash('NewDashApp')

new_dash_app.layout = html.Div([
    dcc.Graph(
        id='new-graph',
        figure={
            'data': [{'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar'}],
            'layout': {'title': 'Sample Bar Chart'}
        }
    )
])
Include the Dash app's route in urls.py using:

path('django_plotly_dash/', include('django_plotly_dash.urls')),
Update or create a Django template to embed the app.

## Embedding Dashboards in Django Templates
Dash apps are embedded using the {% plotly_app %} template tag.

Example (rtv_project/dashboards/templates/dashboards/dashboard_embed.html):

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
Render this template using a Django view to display the embedded dashboard.

## Authentication & Permissions
You can restrict access using Django’s authentication decorators.

Example in dashboards/views.py:

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def dashboard_view(request):
    return render(request, 'dashboards/dashboard_embed.html')
This ensures only authenticated users can access the dashboard.

Troubleshooting
ModuleNotFoundError: No module named 'dpd_static_support'
Ensure you have installed django-plotly-dash.

Include 'dpd_static_support' in INSTALLED_APPS.

Static Files Not Loading
Run:

python manage.py collectstatic
Ensure STATIC_URL, STATICFILES_DIRS, and STATIC_ROOT are correctly configured in settings.py.

Dash Callbacks Not Updating
Check that:

All callbacks are correctly defined.

No runtime exceptions occur during execution.

Input/output IDs match the layout elements.

## Additional Resources
📘 Django Plotly Dash Documentation

📊 Plotly Dash Official Documentation

🔧 Django Official Documentation

End of Dashboard Guide
Crafted with 💡 by Mandela Shaban
