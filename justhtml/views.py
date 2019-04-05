from django.shortcuts import render


def index(request):
    return render(request, "justhtml/index.html")
