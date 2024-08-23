from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *


# Create your views here.
def track_list(request):
    context = {}
    tracks = Track.list_track()
    context["tracks"] = tracks
    return render(request, "track/list.html", context)


def track_create(request):
    context = {}
    if request.method == "POST":
        # validation on the server side
        if (
            len(request.POST["name"]) > 0
            and len(request.POST["name"]) <= 100
            and request.POST["description"]
        ):
            name = request.POST["name"]
            description = request.POST["description"]
            trackobj = Track.create_track(name, description)
            return redirect(trackobj)
        else:
            context["error"] = "Invalid data"

    return render(request, "track/create.html", context)


def track_update(request, id):
    context = {}
    try:
        trackobj = Track.objects.get(id=id)
        if request.method == "POST":
            name = request.POST["name"]
            description = request.POST["description"]
            if len(name) > 0 and len(name) <= 100 and description:
                # trackobj.name = request.POST["name"]
                # trackobj.description = request.POST["description"]
                # trackobj.save()
                # ==============
                # name = request.POST["name"]
                # description = request.POST["description"]
                # save()
                # return redirect("track_list")
                track_url = Track.track_update(id, name, description)
                return redirect(track_url)
            else:
                context["error"] = "Invalid data"
        context["track"] = trackobj
    except Track.DoesNotExist:
        return HttpResponse("Track not found", status=404)

    return render(request, "track/update.html", context)


def track_delete(request, id):
    context = {}
    try:
        if request.method == "GET":
            trackobj = Track.delete_track(id)
            return redirect(trackobj)
    except Track.DoesNotExist:
        return HttpResponse("track not found", status=404)
    return render(request, "track/list.html", context)


def track_details(request, id):
    context = {}
    trackobj = Track.details_track(id)  # Fetch record from the database
    if trackobj is None:
        return HttpResponse("Track not found", status=404)
    context["track"] = trackobj
    return render(request, "track/details.html", context)
