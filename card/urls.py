from django.urls import path
from . import views

app_name = "card"
urlpatterns = [
    path("", views.index, name = "index"),
    path("create/", views.create, name = "create"),
    path("update/<int:note_id>/", views.update, name = "update"),
    path("delete/<int:note_id>/", views.delete, name = "delete"),
]