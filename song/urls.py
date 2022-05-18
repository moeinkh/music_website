from django.urls import path
from . import views

app_name = 'song'

urlpatterns = [
    path('', views.home, name='home'),
    path('about-us/', views.about_us, name='about_us'),
    path('details_song/<str:slug>', views.details_song, name='details_song'),
]