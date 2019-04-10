from django.shortcuts import get_object_or_404, render

from . import models


def index(request):
    texts = models.Text.objects.all()
    return render(request, "textviewer/index.html", {"texts": texts})


def detail(request, slug):
    text = get_object_or_404(models.Text, slug=slug)
    return render(request, "textviewer/detail.html", {"text": text})
