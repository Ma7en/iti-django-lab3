from django.db import models
from django.urls import reverse
import os
from django.conf import settings


# Create your models here.
class Account(models.Model):
    # Account:-
    # - account_id
    # - username
    # - email
    # - password
    # - created_at
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=200)
    image = models.ImageField(upload_to="account/images/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    @staticmethod
    def get_list_url():
        return reverse("account_list")

    def getimage(self):
        return f"/media/{self.image}"

    @classmethod
    def getall(cls):
        return [
            (
                account.id,
                account.username,
                account.email,
                account.password,
                account.image,
                account.created_at,
            )
            for account in cls.objects.all()
        ]

    @classmethod
    def list_account(cls):
        return cls.objects.all()

    @classmethod
    def create_account(cls, username, email, password, image):
        accountobj = cls()
        accountobj.username = username
        accountobj.email = email
        accountobj.password = password
        accountobj.image = image
        accountobj.save()
        return cls.get_list_url()

    @classmethod
    def update_account(cls, id, username, email, password, image):
        accountobj = cls.objects.get(pk=id)
        accountobj.username = username
        accountobj.email = email
        accountobj.password = password

        if image and accountobj.image and accountobj.image != image:
            old_image_path = os.path.join(settings.MEDIA_ROOT, accountobj.image.name)
            if os.path.exists(old_image_path):
                os.remove(old_image_path)

        accountobj.image = image
        accountobj.save()
        return cls.get_list_url()

    @classmethod
    def delete_account(cls, id):
        accountobj = cls.objects.get(pk=id)
        if accountobj.image:
            image_path = os.path.join(settings.MEDIA_ROOT, accountobj.image.name)
            print(f"Attempting to delete image: {image_path}")  # Debugging line
            if os.path.exists(image_path):
                os.remove(image_path)
                print("Image deleted successfully")  # Debugging line
            else:
                print("Image file does not exist")  # Debugging line

        accountobj.delete()
        return cls.get_list_url()

    @classmethod
    def details_account(cls, id):
        return cls.objects.get(pk=id)
