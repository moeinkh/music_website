from django.shortcuts import render, get_object_or_404
from .models import *
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    songs = Song.objects.all().order_by('-created')
    # start pagination config
    paginator = Paginator(songs, 15)
    page_number = request.GET.get('page')
    try:
        page_obj = paginator.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = paginator.page(p.num_pages)
    # end pagination config

    return render(request, 'song/home.html', {
        'songs': page_obj,
    })

def details_song(request, slug):
    song = get_object_or_404(Song, slug=slug)
    return render(request, 'song/details_song.html', {
        'song': song,
        'related_song': Song.objects.filter(singer_song__name=song.get_singer).exclude(id=song.id)[:3],
    })

def about_us(request):
    return render(request, 'song/about_us.html',)

def singers(request, slug):
    singer = Song.objects.filter(singer_song__slug=slug)
    # start pagination config
    paginator = Paginator(singer, 15)
    page_number = request.GET.get('page')
    try:
        page_obj = paginator.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = paginator.page(p.num_pages)
    # end pagination config
    return render(request, 'song/singers.html', {
        'singer': page_obj,
    })

def category(request, slug):
    singer = Song.objects.filter(category_song__slug=slug)
    # start pagination config
    paginator = Paginator(singer, 15)
    page_number = request.GET.get('page')
    try:
        page_obj = paginator.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = paginator.page(p.num_pages)
    # end pagination config
    return render(request, 'song/category.html', {
        'singer': page_obj,
    })