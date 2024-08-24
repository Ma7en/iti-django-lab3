from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import *
from .forms import *
from account.models import *
from track.models import *


# =================================================================
# Create your views here.
def trainee_list(request):
    context = {}
    # traineesobj = Trainee.objects.all()  # Fetch all records from the database
    trainees = Trainee.list_trainee()
    context["trainees"] = trainees
    return render(request, "trainee/list.html", context)


# =================================================================
# def trainee_create(request):
#     context = {}
#     accountsobj = Account.objects.all()  # Fetch all records from the database
#     context["accounts"] = accountsobj

#     tracksobj = Track.objects.all()  # Fetch all records from the database
#     context["tracks"] = tracksobj

#     if request.method == "POST":
#         # validation on the server side
#         if (
#             len(request.POST["first_name"]) > 0
#             and len(request.POST["first_name"]) <= 100
#             and len(request.POST["last_name"]) > 0
#             and len(request.POST["last_name"]) <= 100
#         ):
#             traineeobj = Trainee()
#             traineeobj.first_name = request.POST["first_name"]
#             traineeobj.last_name = request.POST["last_name"]
#             traineeobj.date_of_birth = request.POST["date_of_birth"]
#             traineeobj.account_obj = Account.objects.get(id=request.POST["account_obj"])
#             traineeobj.track_obj = Track.objects.get(id=request.POST["track_obj"])
#             traineeobj.save()
#             return redirect("trainee_list")
#         else:
#             context["error"] = "Invalid data"
#     return render(request, "trainee/create.html", context)


def trainee_create(request):
    context = {}
    form = CreateTrainee()
    context["form"] = form
    if request.method == "POST":
        form = CreateTrainee(request.POST, request.FILES)
        if form.is_valid():
            traineeobj = Trainee.create_trainee(
                form.cleaned_data["first_name"],
                form.cleaned_data["last_name"],
                form.cleaned_data["date_of_birth"],
                form.cleaned_data["image"],
                form.cleaned_data["account_obj"],
                form.cleaned_data["track_obj"],
            )
            return redirect(traineeobj)
        else:
            context["error"] = form.errors
    return render(request, "trainee/create.html", context)


# =================================================================
# def trainee_update(request, id):

#     context = {}
#     traineeobj = ""
#     accountsobj = Account.objects.all()  # Fetch all records from the database
#     context["accounts"] = accountsobj

#     tracksobj = Track.objects.all()  # Fetch all records from the database
#     context["tracks"] = tracksobj

#     try:
#         traineeobj = Trainee.objects.get(id=id)  # Fetch the account to be updated
#     except Trainee.DoesNotExist:
#         return HttpResponse("Trainee not found", status=404)

#     if request.method == "POST":
#         traineeobj.first_name = request.POST["first_name"]
#         traineeobj.last_name = request.POST["last_name"]
#         traineeobj.date_of_birth = request.POST["date_of_birth"]

#         # traineeobj.account_obj = request.POST["account_obj"]
#         # traineeobj.track_obj = request.POST["track_obj"]

#         # Link account and track objects
#         try:
#             account_obj = Account.objects.get(id=request.POST["account_obj"])
#             traineeobj.account_obj = account_obj
#         except Account.DoesNotExist:
#             return HttpResponse("Account not found", status=404)

#         try:
#             track_obj = Track.objects.get(id=request.POST["track_obj"])
#             traineeobj.track_obj = track_obj
#         except Track.DoesNotExist:
#             return HttpResponse("Track not found", status=404)

#         traineeobj.save()
#         return redirect("trainee_list")

#     # Prepopulate the form with current traineeobj data
#     context["trainee"] = traineeobj
#     return render(request, "trainee/update.html", context)


def trainee_update(request, id):
    context = {}
    try:
        traineeobj = Trainee.objects.get(id=id)
        form = UpdateTrainee(
            initial={
                "first_name": traineeobj.first_name,
                "last_name": traineeobj.last_name,
                "date_of_birth": traineeobj.date_of_birth,
                "image": traineeobj.image,
                "account_obj": traineeobj.account_obj,
                "track_obj": traineeobj.track_obj,
            }
        )

        if request.method == "POST":
            form = UpdateTrainee(request.POST, request.FILES)
            if form.is_valid():
                first_name = form.cleaned_data["first_name"]
                last_name = (form.cleaned_data["last_name"],)
                date_of_birth = (form.cleaned_data["date_of_birth"],)

                image = form.cleaned_data.get("image")
                if not image:
                    image = traineeobj.image

                account_obj = Account.objects.get(id=form.cleaned_data["account_obj"])
                track_obj = Track.objects.get(id=form.cleaned_data["track_obj"])

                trainee_url = Trainee.update_trainee(
                    id,
                    first_name,
                    last_name,
                    date_of_birth,
                    image,
                    account_obj,
                    track_obj,
                )
                return redirect(trainee_url)
            else:
                context["error"] = form.errors

        context["form"] = form
        context["trainee"] = traineeobj

    except Trainee.DoesNotExist:
        return HttpResponse("Trainee not found", status=404)

    return render(request, "trainee/update.html", context)


# =================================================================
# def trainee_delete(request, id):
#     context = {}
#     try:
#         traineeobj = Trainee.objects.get(id=id)  # Fetch the trainee to be deleted
#         if request.method == "GET":
#             traineeobj.delete()
#             return redirect("trainee_list")
#         context["trainee"] = traineeobj
#     except Trainee.DoesNotExist:
#         return HttpResponse("Trainee not found", status=404)
#     return render(request, "trainee/list.html", context)


def trainee_delete(request, id):
    try:
        if request.method == "POST":
            Trainee.delete_trainee(id)
            return JsonResponse({"success": True})
    except Trainee.DoesNotExist:
        return JsonResponse(
            {"success": False, "error": "Trainee not found"}, status=404
        )


# =================================================================
# def trainee_details(request, id):
#     context = {}
#     traineeobj = Trainee.objects.get(id=id)  # Fetch record from the database
#     context["trainee"] = traineeobj
#     return render(request, "trainee/details.html", context)


def trainee_details(request, id):
    context = {}
    try:
        traineeobj = Trainee.details_trainee(id)
        context["trainee"] = traineeobj
    except Trainee.DoesNotExist:
        return HttpResponse("Trainee not found", status=404)
    return render(request, "trainee/details.html", context)
