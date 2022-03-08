from django.urls import path

from . import views

app_name = "documents"
urlpatterns = [
    path("", views.index, name="index"),
    path("documents/<int:document_id>", views.download, name="download"),
    path("documents/<int:document_id>/delete", views.delete, name="delete"),
]
