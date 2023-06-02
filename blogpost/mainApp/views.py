from django.shortcuts import render
from myblog.models import myblogpost

def home(request):
    blogData = myblogpost.objects.all().order_by('-id') #Show blog last inserted first
    return render(request,"home.html",{'blogData':blogData})
