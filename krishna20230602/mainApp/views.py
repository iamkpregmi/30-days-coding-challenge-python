from django.shortcuts import render

def home(request):
    return render(request,"index.html")

def result(request):
    data = request.POST.get("name","User")
    data = "Hello " + data
    return render(request,"result.html",{ 'data':data })
