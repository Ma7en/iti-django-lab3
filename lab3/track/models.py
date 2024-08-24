from django.db import models
from django.urls import reverse
import os
from django.conf import settings


# Create your models here.
class Track(models.Model):
    # Track:-
    # - id
    # - name
    # - description
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="track/images/", blank=True, null=True)

    @staticmethod
    def get_list_url():
        return reverse("track_list")

    def getimage(self):
        return f"/media/{self.image}"

    @classmethod
    def getall(cls):
        return [
            (
                track.id,
                track.name,
                track.description,
                track.image,
            )
            for track in cls.objects.all()
        ]

    @classmethod
    def list_track(cls):
        return cls.objects.all()

    @classmethod
    def create_track(cls, name, description, image):
        trackobj = cls()
        trackobj.name = name
        trackobj.description = description
        trackobj.image = image
        trackobj.save()
        return cls.get_list_url()

    @classmethod
    def update_track(cls, id, name, description, image):
        trackobj = cls.objects.get(pk=id)
        trackobj.name = name
        trackobj.description = description

        if image and trackobj.image and trackobj.image != image:
            old_image_path = os.path.join(settings.MEDIA_ROOT, trackobj.image.name)
            if os.path.exists(old_image_path):
                os.remove(old_image_path)

        trackobj.image = image
        trackobj.save()
        return cls.get_list_url()

    @classmethod
    def delete_track(cls, id):
        track = cls.objects.get(pk=id)
        if track.image:
            image_path = os.path.join(settings.MEDIA_ROOT, track.image.name)
            print(f"Attempting to delete image: {image_path}")  # Debugging line
            if os.path.exists(image_path):
                os.remove(image_path)
                print("Image deleted successfully")  # Debugging line
            else:
                print("Image file does not exist")  # Debugging line

        track.delete()
        return cls.get_list_url()

    @classmethod
    def details_track(cls, id):
        return cls.objects.get(pk=id)
