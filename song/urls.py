from django.urls import path
from . import views

app_name = 'song'

urlpatterns = [
    path('', views.home, name='home'),
    path('about-us/', views.about_us, name='about_us'),
    path('contact-us/', views.contact_us, name='contact_us'),
    path('details_song/<str:slug>', views.details_song, name='details_song'),
    path('singer/<str:slug>', views.singers, name='singers'),
    path('category/<str:slug>', views.category, name='category'),
]