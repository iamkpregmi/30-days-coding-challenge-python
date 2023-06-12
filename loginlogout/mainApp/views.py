from django.shortcuts import render
from .models import User_Register

def home(request):
    return render(request,"index.html")

def register(request):
        if request.method == "POST":
            user_name = request.POST.get("username")
            password = request.POST.get("password")
            cpassword = request.POST.get("cpassword")
            name = request.POST.get("name")
            phoneno = request.POST.get("phoneno")
            dob = request.POST.get("dob")
            gender = request.POST.get("gender")
            if password == cpassword:    
                data = User_Register(
                    Username = user_name,
                    Name = name,
                    Phone_No = phoneno,
                    DOB = dob,
                    Gender = gender
                )
                data.save()
        return render(request,"register.html")