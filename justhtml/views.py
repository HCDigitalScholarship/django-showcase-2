"""
The views for the justhtml app.

A view is a function that returns an HTTP response. You could imagine that Django would
just route URLs directly to HTML templates, but if Django did that, there would be no
way to insert information from your database into the template. Views exist mainly for
this reason: to render templates with information from the database.

See textviewer/views.py for some more complicated views.
"""
from django.shortcuts import render


def index(request):
    # Most views end with a call to render and the particular template that the view
    # uses.
    return render(request, "justhtml/index.html")
