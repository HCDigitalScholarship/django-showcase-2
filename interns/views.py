from django.shortcuts import render


def index(request):
    return render(request, "interns/index.html")


def iafisher(request):
    return render(request, "interns/iafisher.html")

def yayad(request):
    return render(request, "interns/yayad.html")
