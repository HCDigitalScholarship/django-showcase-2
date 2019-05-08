"""
The views for the tablebuilder app.

See justhtml/views.py for an explanation of views in Django.
"""
from django.shortcuts import render


def index(request):
    return render(request, "tablebuilder/index.html")
