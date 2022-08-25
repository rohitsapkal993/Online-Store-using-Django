from django.shortcuts import render, HttpResponse
from datetime import datetime
from sensor.models import Contact
# Create your views here.

def index(request):
    context = {
        "ver":"you are graet",
        "ver1" : "your are double graet"
    }
    # return HttpResponse("This is HomePage")
    return render(request,'index.html',context)

def about(request):
    return render(request,'about.html')
    # return HttpResponse("This is About")

def services(request):
    return render(request,'services.html',)
    # return HttpResponse("This is Services")

def contact(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        city = request.POST.get('city')
        zip = request.POST.get('zip')
        contact = Contact(first_name=first_name, last_name=last_name,zip=zip, city=city,)
        contact.save()
    return render(request,'contact.html')
    # return HttpResponse("This is Contact")