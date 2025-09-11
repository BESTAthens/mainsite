from django.urls import include, path
from . import views

urlpatterns=[
    path('',views.home, name='home'),
    path('about/', views.about, name='about' ),
    path('events/',views.events, name='events'),
    path('team/', views.team, name='team' ),
    path('sponsors/',views.sponsors, name='sponsors'),
    path('contact/', views.contact, name='contact' ),
]