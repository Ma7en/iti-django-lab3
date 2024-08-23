from django.db import models
from django.urls import reverse


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
    def track_update(cls, id, name, description, image):
        trackobj = cls.objects.get(pk=id)
        trackobj.name = name
        trackobj.description = description
        trackobj.image = image
        trackobj.save()
        return cls.get_list_url()

    @classmethod
    def delete_track(cls, id):
        cls.objects.filter(pk=id).delete()
        return cls.get_list_url()

    @classmethod
    def details_track(cls, id):
        return cls.objects.get(pk=id)
