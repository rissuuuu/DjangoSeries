from django.urls import path
from . import views
urlpatterns = [
    path('', views.home.as_view(), name='upload'),
    path('upload/',views.upload,name='upload' ),
    path('booklist/',views.book_list,name='booklist' ),
    path('uploadbook/',views.upload_book,name='uploadbook' ),

]