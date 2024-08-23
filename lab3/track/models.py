from django.db import models
from django.urls import reverse
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
import sys


# Create your models here.
class Track(models.Model):
    # Track:-
    # - id
    # - name
    # - description
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()

    @staticmethod
    def get_list_url():
        # return f"/track/{self.id}/"
        # return reverse("track_details", args=[str(self.id)])
        return reverse("track_list")

    @classmethod
    def delete_track(cls, id):
        # ===============================
        # track = get_object_or_404(Track, id=id)
        # if Track.method == "POST":
        #     track.delete()
        #     return redirect(
        #         "track_list"
        #     )  # Redirect to the list of tracks after deletion
        # return render(Track, "track/track_confirm_delete.html", {"track": track})

        # ===============================
        # try:
        #     # Fetch the track to be deleted
        #     track = cls.objects.get(pk=id)
        #     # Delete the track
        #     track.delete()
        #     # Redirect to the track list page
        #     return cls.get_list_url()
        # except Track.DoesNotExist:
        #     return HttpResponse("track not found", status=404)

        # ===============================
        # # Fetch the track to be deleted
        # track = cls.objects.get(pk=id)
        # # Delete the track
        # track.delete()
        # # Redirect to the track list page
        # return cls.get_list_url()

        # ===============================
        cls.objects.filter(pk=id).delete()
        return cls.get_list_url()
