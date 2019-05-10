"""
The views for the interns app.

See justhtml/views.py for an explanation of views in Django.
"""
from django.shortcuts import render


def index(request):
    return render(request, "interns/index.html")


def iafisher(request):
    return render(request, "interns/iafisher.html")


def yayad(request):
    return render(request, "interns/yayad.html")


def mzarafon(request):
    return render(request, "interns/mzarafon.html")


# Add your new intern view here!
