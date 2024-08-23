from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_POST
from .models import *
from .forms import *


# Create your views here.
def track_list(request):
    context = {}
    tracks = Track.list_track()
    context["tracks"] = tracks
    return render(request, "track/list.html", context)


# def track_create(request):
#     context = {}
#     if request.method == "POST":
#         # validation on the server side
#         name = request.POST["name"]
#         description = request.POST["description"]
#         image = request.FILES.get("image")
#         if len(name) > 0 and len(name) <= 100 and description and image:
#             trackobj = Track.create_track(name, description, image)
#             return redirect(trackobj)
#         else:
#             context["error"] = "Invalid data"
#     return render(request, "track/create.html", context)


def track_create(request):
    context = {}
    form = CreateTrack()
    context["form"] = form
    if request.method == "POST":
        # publich data user enter
        form = CreateTrack(request.POST, request.FILES)
        if form.is_valid():
            # create object from book
            trackobj = Track.create_track(
                form.cleaned_data["name"],
                form.cleaned_data["description"],
                form.cleaned_data["image"],
            )
            return redirect(trackobj)
        else:
            context["error"] = form.errors

    return render(request, "track/create.html", context)


def track_update(request, id):
    context = {}
    try:
        trackobj = Track.objects.get(id=id)
        if request.method == "POST":
            name = request.POST["name"]
            description = request.POST["description"]
            image = request.FILES["image"]

            if len(name) > 0 and len(name) <= 100 and description and image:
                track_url = Track.track_update(id, name, description, image)
                return redirect(track_url)
            else:
                context["error"] = "Invalid data"
        context["track"] = trackobj
    except Track.DoesNotExist:
        return HttpResponse("Track not found", status=404)

    return render(request, "track/update.html", context)


def track_delete(request, id):
    # context = {}
    # try:
    #     if request.method == "GET":
    #         trackobj = Track.delete_track(id)
    #         return redirect(trackobj)
    # except Track.DoesNotExist:
    #     return HttpResponse("track not found", status=404)
    # return render(request, "track/list.html", context)
    # ============================================================
    try:
        trackobj = Track.objects.get(pk=id)
        trackobj.delete()
        return JsonResponse({"success": True})
    except Track.DoesNotExist:
        return JsonResponse({"success": False, "error": "Track not found"}, status=404)
    # ============================================================
    # try:
    #     if request.method == "POST":
    #         trackobj = Track.delete_track(id)
    #         trackobj.delete()
    #         return JsonResponse({"success": True})  # استجابة JSON
    # except Track.DoesNotExist:
    #     return JsonResponse({"success": False, "error": "Track not found"}, status=404)


def track_details(request, id):
    context = {}
    trackobj = Track.details_track(id)  # Fetch record from the database
    if trackobj is None:
        return HttpResponse("Track not found", status=404)
    context["track"] = trackobj
    return render(request, "track/details.html", context)
