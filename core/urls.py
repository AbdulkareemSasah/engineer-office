from django.urls import path

from core.views import thome, uhome

app_name = "core"

urlpatterns = [
    path("", thome),
    path("u/", uhome),
]