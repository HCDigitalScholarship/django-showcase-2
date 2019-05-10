"""
The URL configuration for the interns app.

The URL configuration determines how URLs are matched to views, which generate the
server's response. The configuration consists of a Python list called `urlpatterns`.
"""
from django.urls import path

from . import views


app_name = "interns"


# Typically, each element of this list will be a call to Django's path(...) function.
# The expression path("foo", views.foo, name="foo") dictates that the page at the URL
# django-showcase.haverford.edu/foo will display whatever the function foo in the views
# module returns. The name="foo" argument lets you reverse the URL in other parts of the
# code, so that you can write "interns:foo" instead of the whole URL.
urlpatterns = [
    path("", views.index, name="index"),
    path("iafisher", views.iafisher, name="iafisher"),
    path("yayad", views.yayad, name="yayad"),
    path("mzarafon", views.mzarafon, name="mzarafon"),
    # Add your new intern URL here!
]
