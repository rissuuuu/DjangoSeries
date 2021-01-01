from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
import os
class home(TemplateView):
    template_name='home.html'



def upload(request):
    if request.method=='POST':
        upload_file=request.FILES['document']
        fs=FileSystemStorage()
        name=fs.save(upload_file.name,upload_file)
        url=fs.url(name)
        print(url)
    return render(request,'upload.html')

