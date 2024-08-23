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
        return reverse("track_list")

    @classmethod
    def list_track(cls):
        return cls.objects.all()
        # return cls.get_list_url()

    @classmethod
    def create_track(cls, name, description):
        trackobj = cls()
        trackobj.name = name
        trackobj.description = description
        trackobj.save()
        return cls.get_list_url()

    def track_update(self):
        pass

    @classmethod
    def delete_track(cls, id):
        cls.objects.filter(pk=id).delete()
        return cls.get_list_url()

    @classmethod
    def details_track(cls, id):
        pass
