from django.db import models


# Create your models here.
class Track(models.Model):
    # Track:-
    # - id
    # - name
    # - description
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
