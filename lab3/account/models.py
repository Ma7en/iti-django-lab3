from django.db import models


# Create your models here.
class Account(models.Model):
    # Account:-
    # - account_id
    # - username
    # - password
    # - email
    # - created_at
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=200)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
