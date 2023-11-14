from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee
# Create your views here.

def application(request):
    if request.method == "POST":
        name = request.POST["name"]
        id = request.POST["id"]
        email = request.POST["email"]
        domain =request.POST["domain"]

        employee = Employee(name=name,id=id,email=email,domain=domain)
        employee.save()
    return render(request,"index.html")
    # return HttpResponse("Hello World")
