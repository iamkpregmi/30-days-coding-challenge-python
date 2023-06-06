from django.shortcuts import render
from django.http import HttpResponse
from .models import userlogin

def home(request):
    return render(request,"index.html")

def dashboard(request):
    if request.method == "POST":
        userid = request.POST.get("userid")
        pwd = request.POST.get("pwd")
        mydata = userlogin.objects.filter(userid=userid)
        print(mydata.userid)
        return render(request,"dashboard.html")    
        # if userid == mydata.userid and pwd == mydata.password:
        #     return render(request,"dashboard.html",{"msg": "krishna"})
        
