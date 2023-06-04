from django.shortcuts import render
from .models import Result

def home(request):
    Name = request.POST.get("name")
    if request.method == "POST":
        Student_Result = Result.objects.filter(Name=Name)
    else:    
        Student_Result = Result.objects.all()
    return render(request,"index.html",{"Student_Result": Student_Result})

def about(request):
    return render(request,"about.html")