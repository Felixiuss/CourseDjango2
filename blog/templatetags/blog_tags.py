from django import template
# from django.utils.translation import get_language

from blog.models import Category

register = template.Library()  # регистрация templates


def get_categories(context, order, count):
    """Получаю список Категорий"""
    categories = Category.objects.filter(published=True).order_by(order)  #parent__isnull=True
    if count is not None:  # if count
        categories = categories[:count]
    return categories


@register.inclusion_tag('base/tags/base_tag.html', takes_context=True)
def category_list(context, order='-name', count=None, template='base/blog/categories.html'):
    """template taf вывода категорий"""
    categories = get_categories(context, order, count)
    return {'template': template, 'category_list': categories}


@register.simple_tag(takes_context=True)
def for_category_list(context, count=None, order='-name'):
    """template tag вывода категорий без шаблона"""
    return get_categories(context, order, count)
