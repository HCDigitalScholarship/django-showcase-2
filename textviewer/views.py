"""
The views for the interns app.

See justhtml/views.py for an introductory explanation of views in Django. This module
has slightly more complex views, because it actually needs to query the database.
"""
from django.shortcuts import get_object_or_404, render

from . import models


def index(request):
    # Query the database to get all the texts.
    texts = models.Text.objects.all()
    # Pass the texts as an argument to the template renderer. In the template itself,
    # we can access the text's using Django's templating language.
    return render(request, "textviewer/index.html", {"texts": texts})


def detail(request, slug):
    # Similar to the index view, except it fetches a single text instead of all of them.
    text = get_object_or_404(models.Text, slug=slug)
    return render(request, "textviewer/detail.html", {"text": text})
