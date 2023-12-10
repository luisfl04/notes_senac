from django.urls import path, include



urlpatterns = [
    path("contas/", include("django.contrib.auth.urls")),
]