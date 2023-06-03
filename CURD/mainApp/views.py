from django.shortcuts import render,redirect
from .models import Employee

def home(request):
    table_data = Employee.objects.all()
    return render(request,"home.html",{"table_data": table_data})

def add(request):
    if (request.method == "POST"):
        e = Employee()
        e.name = request.POST.get('name')
        e.email = request.POST.get('email')
        e.phone = request.POST.get('phone')
        e.salary = request.POST.get('salary')
        e.city = request.POST.get('city')
        e.save()
        return redirect("/")
    return render(request,"add.html")

def update(request,id):
    table_data = Employee.objects.get(id=id)
    if (request.method == "POST"):
        table_data.name = request.POST.get('name')
        table_data.email = request.POST.get('email')
        table_data.phone = request.POST.get('phone')
        table_data.salary = request.POST.get('salary')
        table_data.city = request.POST.get('city')
        table_data.save()
        return redirect("/")
    return render(request,"update.html",{"table_data":table_data})

def delete(request,id):
    table_data = Employee.objects.get(id=id)
    if(table_data):
        table_data.delete()
    return redirect("/")
