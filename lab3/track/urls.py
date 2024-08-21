from django.urls import path
from .views import *

urlpatterns = [
    path("", track_list, name="track_list"),
    path("Add/", track_create, name="track_create"),
    path("Update/<int:id>", track_update, name="track_update"),
    path("Delete/<int:id>", track_delete, name="track_delete"),
    path("Details/<int:id>", track_details, name="track_details"),
]
