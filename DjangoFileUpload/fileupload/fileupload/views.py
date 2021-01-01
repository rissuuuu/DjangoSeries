from django.shortcuts import render
from django.views.generic import TemplateView

class home(TemplateView):
    template_name='home.html'



def upload(request):
    if request.method=='POST':
        upload_file=request.FILES['document']
        print(upload_file.name)
        print(upload_file.size)
    return render(request,'upload.html')

