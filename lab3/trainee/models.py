from django.db import models
from account.models import *
from track.models import *


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
    account_obj = models.ForeignKey("account.Account", on_delete=models.CASCADE)
    track_obj = models.ForeignKey("track.Track", on_delete=models.CASCADE)
