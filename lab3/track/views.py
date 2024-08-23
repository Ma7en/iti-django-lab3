from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *


# Create your views here.
def track_list(request):
    context = {}
    tracks = Track.objects.all()
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
            accountobj = Track()
            accountobj.name = request.POST["name"]
            accountobj.description = request.POST["description"]
            accountobj.save()
            return redirect("track_list")
        else:
            context["error"] = "Invalid data"

    return render(request, "track/create.html", context)


def track_update(request, id):
    context = {}
    try:
        trackobj = Track.objects.get(id=id)  # Fetch the account to be updated
        if request.method == "POST":
            if (
                len(request.POST["name"]) > 0
                and len(request.POST["name"]) <= 100
                and request.POST["description"]
            ):
                trackobj.name = request.POST["name"]
                trackobj.description = request.POST["description"]
                trackobj.save()
                return redirect("track_list")
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

    # ===============================
    # Track.delete_track(id)

    # ===============================
    # context = {}
    # try:
    #     trackobj = Track.objects.get(id=id)  # Fetch the trainee to be deleted
    #     if request.method == "GET":
    #         trackobj.delete()
    #         return redirect("track_list")
    #     context["track"] = trackobj
    # except Track.DoesNotExist:
    #     return HttpResponse("track not found", status=404)
    # return render(request, "track/delete.html", context)


def track_details(request, id):
    context = {}
    trackobj = Track.objects.get(id=id)  # Fetch record from the database
    context["track"] = trackobj
    return render(request, "track/details.html", context)
