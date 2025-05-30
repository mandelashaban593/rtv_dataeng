from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.contrib.auth import views as auth_views
from dashboards.views import dashboard_view

urlpatterns = [
    path('admin/', admin.site.urls),

    # Login/Logout
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='/accounts/login/'), name='logout'),

    # Redirect base URL to dashboard page
    path('', RedirectView.as_view(url='/dashboard/', permanent=False)),

    # Dashboard embed page (with login required)
    path('dashboard/', dashboard_view, name='dashboard'),

    # Django Plotly Dash apps (JS, data, etc)
    path('django_plotly_dash/', include('django_plotly_dash.urls')),
]
