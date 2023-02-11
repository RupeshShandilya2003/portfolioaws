from django.shortcuts import render,HttpResponse
from home import models

# Create your views here.

def home(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        ins = models.homes(name = name,email=email,message=message)
        ins.save()
        print("Posted to DB") #used for debugging
    return render(request,'index.html')