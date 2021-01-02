from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from .forms import BookForm
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

def book_list(request):
    return render(request,'book_list.html')

def upload_book(request):
    form=BookForm()
    return render(request,'upload_book.html',{
        'form':form
    })