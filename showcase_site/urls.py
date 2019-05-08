"""
The root URL configuration for the showcase site.

The main purpose of this file is to pull in the URL configurations for each individual
app, as well as Django's built-in admin URLs.
"""
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("justhtml.urls")),
    path("interns/", include("interns.urls")),
    path("texts/", include("textviewer.urls")),
    path("tablebuilder/", include("tablebuilder.urls")),
]
