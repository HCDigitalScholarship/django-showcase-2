"""
The URL configuration for the textviewer app.

See interns/urls.py for an explanation of how URL configuration works.
"""
from django.urls import path

from . import views


app_name = "textviewer"


urlpatterns = [
    path("", views.index, name="index"),
    path("<slug:slug>/", views.detail, name="detail"),
]
