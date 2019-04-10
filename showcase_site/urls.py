from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("justhtml.urls")),
    path("texts/", include("textviewer.urls")),
]
