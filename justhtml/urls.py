"""
The URL configuration for the justhtml app.

See interns/urls.py for an explanation of how URL configuration works.
"""
from django.urls import path

from . import views


app_name = "justhtml"


urlpatterns = [path("", views.index, name="index")]
