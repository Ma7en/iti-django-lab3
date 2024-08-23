from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from account.models import *
from track.models import *


# Create your views here.
def trainee_list(request):
    context = {}
    traineesobj = Trainee.objects.all()  # Fetch all records from the database
    context["trainees"] = traineesobj
    return render(request, "trainee/list.html", context)


def trainee_create(request):
    context = {}
    accountsobj = Account.objects.all()  # Fetch all records from the database
    context["accounts"] = accountsobj

    tracksobj = Track.objects.all()  # Fetch all records from the database
    context["tracks"] = tracksobj

    if request.method == "POST":
        # validation on the server side
        if (
            len(request.POST["first_name"]) > 0
            and len(request.POST["first_name"]) <= 100
            and len(request.POST["last_name"]) > 0
            and len(request.POST["last_name"]) <= 100
        ):
            traineeobj = Trainee()
            traineeobj.first_name = request.POST["first_name"]
            traineeobj.last_name = request.POST["last_name"]
            traineeobj.date_of_birth = request.POST["date_of_birth"]
            traineeobj.account_obj = Account.objects.get(id=request.POST["account_obj"])
            traineeobj.track_obj = Track.objects.get(id=request.POST["track_obj"])
            traineeobj.save()
            return redirect("trainee_list")
        else:
            context["error"] = "Invalid data"

    return render(request, "trainee/create.html", context)


def trainee_update(request, id):

    context = {}
    traineeobj = ""
    accountsobj = Account.objects.all()  # Fetch all records from the database
    context["accounts"] = accountsobj

    tracksobj = Track.objects.all()  # Fetch all records from the database
    context["tracks"] = tracksobj

    try:
        traineeobj = Trainee.objects.get(id=id)  # Fetch the account to be updated
    except Trainee.DoesNotExist:
        return HttpResponse("Trainee not found", status=404)

    if request.method == "POST":
        traineeobj.first_name = request.POST["first_name"]
        traineeobj.last_name = request.POST["last_name"]
        traineeobj.date_of_birth = request.POST["date_of_birth"]

        # traineeobj.account_obj = request.POST["account_obj"]
        # traineeobj.track_obj = request.POST["track_obj"]

        # Link account and track objects
        try:
            account_obj = Account.objects.get(id=request.POST["account_obj"])
            traineeobj.account_obj = account_obj
        except Account.DoesNotExist:
            return HttpResponse("Account not found", status=404)

        try:
            track_obj = Track.objects.get(id=request.POST["track_obj"])
            traineeobj.track_obj = track_obj
        except Track.DoesNotExist:
            return HttpResponse("Track not found", status=404)

        traineeobj.save()
        return redirect("trainee_list")

    # Prepopulate the form with current traineeobj data
    context["trainee"] = traineeobj

    return render(request, "trainee/update.html", context)


def trainee_delete(request, id):
    context = {}
    try:
        traineeobj = Trainee.objects.get(id=id)  # Fetch the trainee to be deleted
        if request.method == "GET":
            traineeobj.delete()
            return redirect("trainee_list")
        context["trainee"] = traineeobj
    except Trainee.DoesNotExist:
        return HttpResponse("Trainee not found", status=404)

    return render(request, "trainee/list.html", context)


def trainee_details(request, id):
    context = {}
    traineeobj = Trainee.objects.get(id=id)  # Fetch record from the database
    context["trainee"] = traineeobj
    return render(request, "trainee/details.html", context)
