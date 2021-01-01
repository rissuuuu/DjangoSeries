from django.urls import path
from . import views
urlpatterns = [
    path('', views.intialize, name='check'),
    path('check/', views.check,name='check'),

]
