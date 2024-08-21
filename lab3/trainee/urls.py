from django.urls import path
from .views import *

urlpatterns = [
    path("", trainee_list, name="trainee_list"),
    path("Add/", trainee_create, name="trainee_create"),
    path("Update/<int:id>", trainee_update, name="trainee_update"),
    path("Delete/<int:id>", trainee_delete, name="trainee_delete"),
    path("Details/<int:id>", trainee_details, name="trainee_details"),
]
