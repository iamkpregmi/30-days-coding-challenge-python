from django.shortcuts import render
from .models import Student_Grade_Card

def home(request):
    return render(request,"index.html")

def result(request):
    if request.method == "GET":
        Roll_No = request.GET.get("enrollment_number")
        Student_Data = Student_Grade_Card.objects.filter(Roll_No=Roll_No)
        total = 0
        for i in Student_Data:
            total = i.Physics + i.Chemistry + i.Maths + i.English + i.Computer_Science
        percentage = (total/500)*100
        Student_Data = {
            'Student_Data':Student_Data,
            'total': total,
            'percentage': percentage,
        }
    return render(request,"result.html",Student_Data)
