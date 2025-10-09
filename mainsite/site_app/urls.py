from django.urls import include, path
from . import views

urlpatterns=[
    path('',views.home, name='home'),
    path('about/', views.about, name='about' ),
    path('events/',views.events, name='events'),
    path('team/', views.team, name='team' ),
    path('sponsors/',views.sponsors, name='sponsors'),
    path('contact/', views.contact, name='contact' ),
    path("join-us/", views.joinus, name="join_us"),
    path("clue1/", views.clue1, name="clue1"),
    path("clue2/", views.clue2, name="clue2"),
    path("clue3/", views.clue3, name="clue3"),
    path("clue4/", views.clue4, name="clue4"),
    path("clue4/42/", views.IT, name="IT"),
]