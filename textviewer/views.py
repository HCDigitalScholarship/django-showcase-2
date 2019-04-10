from django.shortcuts import render

from . import models


def index(request):
    texts = models.Text.objects.all()
    return render(request, "textviewer/index.html", {"texts": texts})
