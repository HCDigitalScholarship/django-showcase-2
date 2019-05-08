"""
The URL configuration for the tablebuilder app.

See justhtml/urls.py for an explanation of how URL configuration works.
"""
from django.urls import path

from . import views


app_name = "tablebuilder"


urlpatterns = [path("", views.index, name="index")]
