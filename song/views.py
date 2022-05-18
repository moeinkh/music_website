from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.
def home(request):
    return render(request, 'song/home.html', {
        'singers': Singer.objects.all(),
        'categories': Category.objects.all(),
        'songs': Song.objects.all().order_by('-created'),
    })

def details_song(request, slug):
    song = get_object_or_404(Song, slug=slug)
    print(song.get_singer)
    return render(request, 'song/details_song.html', {
        'song': song,
        'singers': Singer.objects.all(),
        'categories': Category.objects.all(),
        'related_song': Song.objects.filter(singer_song__name=song.get_singer).exclude(id=song.id)[:3],
    })

def about_us(request):
    return render(request, 'song/about_us.html', {
        'singers': Singer.objects.all(),
        'categories': Category.objects.all(),
    })    