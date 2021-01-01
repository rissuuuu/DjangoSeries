from django.shortcuts import render

# Create your views here.




from django.http import HttpResponse

def intialize(request):
    return HttpResponse("Website is up")

def check(request):
    return render(request,'shopping/index.html')