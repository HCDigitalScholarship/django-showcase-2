"""
The views for the interns app.

A view is a function that returns an HTTP response. You could imagine that Django would
just route URLs directly to HTML templates, but if Django did that, there would be no
way to insert information from your database into the template. Views exist mainly for
this reason: to render templates with information from the database.

See textviewer/views.py for some more complicated views.
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


def cstuartroe(request):
    return render(request, "interns/cstuartroe.html")


# Add your new intern view here!
