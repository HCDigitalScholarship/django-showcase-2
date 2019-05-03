from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("justhtml.urls")),
    path("interns/", include("interns.urls")),
    path("texts/", include("textviewer.urls")),
    path("tablebuilder/", include("tablebuilder.urls")),
]
