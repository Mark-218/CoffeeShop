from django.shortcuts import render, HttpResponse
from CoffeeHouse.models import Contact
# Create your views here.

# def index(request):
#     return HttpResponse("This is Home Page")

def index(request):
     return render(request, "index.html")

def about(request):
     return render(request, "about.html")

def contact(request):
     if request.method == "POST":
          name = request.POST.get('name')
          email = request.POST.get('email')
          phone = request.POST.get('phone')
          desc = request.POST.get('desc')
          contact = Contact(name=name, email=email, phone=phone, desc=desc)
          contact.save()
     return render(request, "contact.html")

def pricing(request):
     return render(request, "pricing.html")