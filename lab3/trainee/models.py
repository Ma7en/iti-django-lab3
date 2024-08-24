from django.db import models
from account.models import *
from track.models import *
from django.urls import reverse
import os
from django.conf import settings


# Create your models here.
class Trainee(models.Model):
    # trainee
    # - trainee_id
    # - first_name
    # - last_name
    # - data_of_birth
    # - account_id
    # - track_id
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    image = models.ImageField(upload_to="track/images/", blank=True, null=True)
    account_obj = models.ForeignKey("account.Account", on_delete=models.CASCADE)
    track_obj = models.ForeignKey("track.Track", on_delete=models.CASCADE)

    @staticmethod
    def get_list_url():
        return reverse("trainee_list")

    def getimage(self):
        return f"/media/{self.image}"

    @classmethod
    def list_trainee(cls):
        return cls.objects.all()

    @classmethod
    def create_trainee(
        cls,
        first_name,
        last_name,
        date_of_birth,
        image,
        account_obj,
        track_obj,
    ):
        traineeobj = cls()
        traineeobj.first_name = first_name
        traineeobj.last_name = last_name
        traineeobj.date_of_birth = date_of_birth
        traineeobj.image = image
        traineeobj.account_obj = account_obj
        traineeobj.track_obj = track_obj
        traineeobj.save()
        return cls.get_list_url()

    @classmethod
    def update_trainee(
        cls,
        id,
        first_name,
        last_name,
        date_of_birth,
        image,
        account_obj,
        track_obj,
    ):
        traineeobj = cls.objects.get(pk=id)
        traineeobj.first_name = first_name
        traineeobj.last_name = last_name
        traineeobj.date_of_birth = date_of_birth

        if image and traineeobj.image and traineeobj.image != image:
            old_image_path = os.path.join(settings.MEDIA_ROOT, traineeobj.image.name)
            if os.path.exists(old_image_path):
                os.remove(old_image_path)

        traineeobj.image = image
        traineeobj.account_obj = account_obj
        traineeobj.track_obj = track_obj
        traineeobj.save()
        return cls.get_list_url()

    @classmethod
    def delete_trainee(cls, id):
        traineeobj = cls.objects.get(pk=id)
        if traineeobj.image:
            image_path = os.path.join(settings.MEDIA_ROOT, traineeobj.image.name)
            print(f"Attempting to delete image: {image_path}")  # Debugging line
            if os.path.exists(image_path):
                os.remove(image_path)
                print("Image deleted successfully")  # Debugging line
            else:
                print("Image file does not exist")  # Debugging line

        traineeobj.delete()
        return cls.get_list_url()

    @classmethod
    def details_trainee(cls, id):
        return cls.objects.get(pk=id)
