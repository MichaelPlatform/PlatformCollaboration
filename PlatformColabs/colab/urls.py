from django.contrib import admin
from django.urls import path
from .views import groupsapi, teamsapi, companyapi

urlpatterns = [
    path('admin/', admin.site.urls),
    path('groups/', groupsapi),
    path('teams/', teamsapi),
    path('businesses/', companyapi),
]
