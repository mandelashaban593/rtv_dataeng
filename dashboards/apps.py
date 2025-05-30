# dashboards/apps.py
from django.apps import AppConfig

class DashboardsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dashboards'

    def ready(self):
        # 👇 This line is **critical**: it ensures your Dash app registers on startup.
        import dashboards.dash_apps
