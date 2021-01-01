



from django.http import HttpResponse

def check(request):
    return HttpResponse("This is temp website")

def initialize(request):
    return HttpResponse("This is your website")