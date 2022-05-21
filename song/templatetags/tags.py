from django import template
from ..models import Category, Singer

register = template.Library()


@register.inclusion_tag('song/categories_tags.html')
def show_categories(categories):
    categories = Category.objects.all()
    return {'categories': categories}


@register.inclusion_tag('song/singers_tags.html')
def show_singers(singers):
    singers = Singer.objects.all()
    return {'singers': singers}