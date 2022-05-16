from django.db import models

# Create your models here.
class Date(models.Model):
    created = models.DateTimeField(
        'زمان ایجاد',
        auto_now_add=True,
        )
    updated = models.DateTimeField(
        'زمان اپدیت',
        auto_now=True,
        )


class Category(Date):
    
    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    title = models.CharField(
        'عنوان',
        max_length=64,
        )
    slug = models.SlugField(
        'اسلاگ',
        max_length=64,
        )   

    def __str__(self):
        return self.title


class Singer(Date):

    class Meta:
        verbose_name = 'خواننده'
        verbose_name_plural = 'خوانندگان'

    name = models.CharField(
        'نام خواننده',
        max_length=128,
        )    
    slug = models.SlugField(
        'اسلاگ',
        max_length=128,
        )

    def __str__(self):
        return self.name

class Album(Date):

    class Meta:
        verbose_name = 'آلبوم'
        verbose_name_plural = 'آلبوم ها'

    title = models.CharField(
        'عنوان آلبوم',
        max_length=128,
        )
    slug = models.SlugField(
        'اسلاگ',
        max_length=128,
        )    
    singer_album = models.ForeignKey(
        Singer, 
        on_delete=models.CASCADE, 
        related_name='item_album',
        verbose_name='خواننده'
        ) 
    poster = models.ImageField(
        'پوستر آلبوم',
        upload_to='poster_album/',
        )  

    def __str__(self):
        return self.title                      


class Song(Date):

    class Meta:
        verbose_name = 'آهنگ'
        verbose_name_plural = 'آهنگ ها'

    album_song = models.ForeignKey(
        Album,
        on_delete=models.CASCADE,
        related_name='item_song',
        null=True,
        blank=True,
        verbose_name='آلبوم',
        )
    singer_song = models.ManyToManyField(
        Singer,
        related_name='song_singer',
        verbose_name='خواننده',
        ) 
    title = models.CharField(
        'عنوان آهنگ',
        max_length=64,
        )
    slug = models.SlugField(
        'اسلاگ',
        max_length=64,
        )    
    text = models.TextField(
        'متن آهنگ',
        null=True,
        blank=True, 
        )
    poster = models.ImageField(
        'پوستر آهنگ',
        upload_to='poster_song/',
        )

    def get_singer(self):
        return '\n'.join([i.nama for i in self.singer_song.all()])    

    def __str__(self):
        return self.title    