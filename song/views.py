from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.core.paginator import Paginator
from .forms import ContactForm, CommentForm
from django.contrib import messages
from django.db.models import Q

# Create your views here.
def home(request, slug=None):
    songs = Song.objects.all().order_by('-created')
    search = request.GET.get('search')
    if search:
        songs = songs.filter(Q(text__contains=search) | Q(title__contains=search) | Q(singer_song__name__contains=search))

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
    if request.method == 'POST':
        url = request.META.get('HTTP_REFERER')
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment()
            comment.song_comment = song
            comment.name = form.cleaned_data['name']
            comment.email = form.cleaned_data['email']
            comment.text = form.cleaned_data['text']
            comment.save()
            messages.success(request, 'نظر شما با موفقیت ثبت شد.')
            return redirect(url)
    else:
        form = CommentForm()

    return render(request, 'song/details_song.html', {
        'song': song,
        'related_song': Song.objects.filter(singer_song__name=song.get_singer).exclude(id=song.id)[:3],
        'comments': Comment.objects.filter(active=True, song_comment=song).order_by('-created'),
    })

def about_us(request):
    return render(request, 'song/about_us.html')

def contact_us(request):
    if request.method == 'POST':
        url = request.META.get('HTTP_REFERER')
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'پیام شما با موفقیت ثبت شد.')
            return redirect(url)
    else:
        form = ContactForm()     
    return render(request, 'song/contact_us.html')

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