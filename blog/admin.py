from django.contrib import admin

from .models import Category, Post, Tag, Comment
from pages.admin import ActionPublish


class CategoryAdmin(ActionPublish):
    """ Категории блога"""
    list_display = ('id', 'name', 'parent', 'slug', 'paginated', 'sort', 'published')
    list_display_links = ('name', )  # делает ссылкой поле - 'name
    list_filter = ('parent', )
    actions = ['unpublish', 'publish']


class CommentsInline(admin.StackedInline):
    """Вставка возможности добавления/удалениы комментариев в модель Post"""
    model = Comment
    extra = 1


class PostAdmin(ActionPublish):
    """Посты блога"""
    inlines = [CommentsInline]  # вставка комментариев
    filter_horizontal = ("tags",)  # видоизменяет виджет many-to-many
    fieldsets = (
        ('Контент', {
            'fields': ('author', 'title', 'subtitle', 'slug'),
        }),
        ('Контент 2', {
            'fields': ('mini_text', 'text', 'image'),
        }),
        ('Даты', {
            'fields': ('edit_date', 'published_date'),
        }),
        ('Завязки', {
            'classes': ('wide', 'extrapretty'),
            'fields': ('tags', 'category'),
        }),
        ('Настройки', {
            'classes': ('collapse',),  # сворачивает настройки
            'fields': ('template', 'published', 'status', 'sort', 'viewed'),
        }),
    )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(Comment)


admin.site.site_title = "Course django 2"  # замена заголовка
admin.site.site_header = "Course django 2"