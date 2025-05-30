# dashboards/dash_apps.py

from django_plotly_dash import DjangoDash
from dash import html, dcc
import plotly.express as px
import pandas as pd

# Dummy data
df = pd.DataFrame({
    'Year': ['Baseline', 'Year 1', 'Year 2'],
    'Poverty Rate': [0.45, 0.35, 0.30],
    'Households Surveyed': [5000, 4800, 4600],
})

# Register app using the **exact name** you refer to in your template or URL
app = DjangoDash("poverty_dashboard")  # 👈 this name must match

app.layout = html.Div([
    html.H2("Poverty Dashboard", style={"textAlign": "center"}),

    dcc.Graph(
        figure=px.line(df, x='Year', y='Poverty Rate', markers=True)
    )
])
