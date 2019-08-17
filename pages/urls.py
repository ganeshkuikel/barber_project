from django.urls import path

from . import views

urlpatterns=[path('',views.index,name='index'),
             path('about',views.about,name='about'),
             path('appointment',views.appointment,name='appointment'),
             path('services',views.services,name='services'),
             path('barbers',views.barbers,name='barbers'),
             path('contact',views.contact,name='contact'),]