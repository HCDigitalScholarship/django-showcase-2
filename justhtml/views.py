"""
The views for the justhtml app.

See interns/views.py for an explanation of views in Django.
"""
from django.shortcuts import render


def index(request):
    # Most views end with a call to render and the particular template that the view
    # uses.
    return render(request, "justhtml/index.html")
