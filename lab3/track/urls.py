from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", track_list, name="track_list"),
    path("Add/", track_create, name="track_create"),
    path("Update/<int:id>", track_update, name="track_update"),
    path("Delete/<int:id>", track_delete, name="track_delete"),
    path("Details/<int:id>", track_details, name="track_details"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
