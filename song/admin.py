from django.contrib import admin
from .models import Date, Category, Singer, Album, Song, Contact, Comment

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'created'
    )

    prepopulated_fields = {'slug': ('title',)}

class SingerAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'created',
    )

    list_filter = (
        'name',
    )

    search_fields = (
        'name',
    )

    prepopulated_fields = {'slug': ('name',)}

class AlbumAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'singer_album',
        'created',
    )
    list_filter = (
        'title',
        'singer_album',
    )

    prepopulated_fields = {'slug': ('title',)}

class SongAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'created',
        'get_singer',
    )
    list_filter = (
        'title',
    )
    search_fields = (
        'title',
        'get_singer',
    )

    filter_horizontal = (
        'singer_song',
    )
    prepopulated_fields = {'slug': ('title',)}

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'created')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'song_comment','created', 'active')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Singer, SingerAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Song, SongAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Comment, CommentAdmin)