import dash
from dash import html, dcc
import plotly.express as px
from django_plotly_dash import DjangoDash
import pandas as pd
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from analysis.metrics import all_metrics  # use correct function

# Dummy data
data = {
    'Year': ['Baseline', 'Year 1', 'Year 2'],
    'Poverty Rate': [0.45, 0.35, 0.30],
    'Households Surveyed': [5000, 4800, 4600],
}
df = pd.DataFrame(data)
def get_metrics():
    try:
        return all_metrics()
    except Exception as e:
        print("Metric computation error:", e)
        return {
            'Average Income': 0,
            'Average Expenditure': 0,
            'Poverty Headcount Ratio': 0,
            'Food Insecurity Rate': 0,
            'Latrine Access Rate': 0,
            'Water Access Rate': 0,
            'School Enrollment Rate': 0,
        }

metrics = get_metrics()

app = DjangoDash('poverty_dashboard')

app.layout = html.Div([
    html.H1("RTV Poverty Metrics Dashboard", style={'textAlign': 'center'}),

    dcc.Graph(
        id='poverty-rate-trend',
        figure=px.line(
            df,
            x='Year',
            y='Poverty Rate',
            title='Poverty Rate Trend Over Survey Cycles',
            markers=True,
            labels={'Poverty Rate': 'Poverty Rate (%)'}
        )
    ),

    dcc.Graph(
        id='households-surveyed',
        figure=px.bar(
            df,
            x='Year',
            y='Households Surveyed',
            title='Number of Households Surveyed',
            labels={'Households Surveyed': 'Count'}
        )
    ),

    html.Div([
        html.H3("Key Derived Metrics"),
        html.Ul([
            html.Li(f"Average Income: {metrics['Average Income']:.2f}"),
            html.Li(f"Average Expenditure: {metrics['Average Expenditure']:.2f}"),
            html.Li(f"Poverty Headcount Ratio: {metrics['Poverty Headcount Ratio']:.2%}"),
            html.Li(f"Food Insecurity Rate: {metrics['Food Insecurity Rate']:.2%}"),
            html.Li(f"Latrine Access Rate: {metrics['Latrine Access Rate']:.2%}"),
            html.Li(f"Water Access Rate: {metrics['Water Access Rate']:.2%}"),
            html.Li(f"School Enrollment Rate: {metrics['School Enrollment Rate']:.2%}"),
        ])
    ], style={'marginTop': 20, 'fontSize': '18px'})
])

@login_required
def dashboard_view(request):
    return render(request, "dashboards/dashboard_embed.html")
