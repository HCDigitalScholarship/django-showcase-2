from django.urls import path

from . import views


app_name = "justhtml"


urlpatterns = [path("", views.index, name="index")]
