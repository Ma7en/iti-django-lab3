from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", account_list, name="account_list"),
    path("Add/", account_create, name="account_create"),
    path("Update/<int:id>", account_update, name="account_update"),
    path("Delete/<int:id>", account_delete, name="account_delete"),
    path("Details/<int:id>", account_details, name="account_details"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
