from django.shortcuts import render,redirect
from .models import foodExercise

def home(request):
    return render(request,"index.html")

def add_data(request):
    Fname = request.POST.get("name")
    Femail = request.POST.get("email")
    Fmessage = request.POST.get("message")

    obj = foodExercise.objects.create(Cname=Fname,Cemail=Femail,Cmessage=Fmessage)
    obj.save()
    return redirect("/")