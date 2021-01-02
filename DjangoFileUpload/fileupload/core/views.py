from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from .forms import BookForm

from .models import Book
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
    books=Book.objects.all()
    return render(request,'book_list.html',{
        'books':books
    })

def upload_book(request):
    if request.method=='POST':
        up_file=request.FILES
        form=BookForm(request.POST,up_file)
        form.loc='books/pdfs/'+str(up_file)
        if form.is_valid():
            form.save()
            return redirect('booklist')
    else:
        form=BookForm()
    return render(request,'upload_book.html',{
        'form':form
    })