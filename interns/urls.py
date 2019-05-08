"""
The URL configuration for the interns app.

See justhtml/urls.py for an explanation of how URL configuration works.
"""
from django.urls import path

from . import views


app_name = "interns"


urlpatterns = [
    path("", views.index, name="index"),
    path("iafisher", views.iafisher, name="iafisher"),
    path("yayad", views.yayad, name="yayad"),
    # Add your new intern URL here!
]
