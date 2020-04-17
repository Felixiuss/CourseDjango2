# Generated by Django 2.2.7 on 2020-03-29 19:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.TextField(blank=True, default='', max_length=1000, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='category',
            name='paginated',
            field=models.PositiveIntegerField(default=5, verbose_name='Количество новостей на странице'),
        ),
        migrations.AddField(
            model_name='category',
            name='published',
            field=models.BooleanField(default=True, verbose_name='Отображать?'),
        ),
        migrations.AddField(
            model_name='category',
            name='sort',
            field=models.PositiveIntegerField(default=0, verbose_name='Порядок'),
        ),
        migrations.AddField(
            model_name='category',
            name='template',
            field=models.CharField(default='blog/post_list.html', max_length=500, verbose_name='Шаблон'),
        ),
        migrations.AddField(
            model_name='post',
            name='edit_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Дата редактирования'),
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='post/', verbose_name='Главная фотография'),
        ),
        migrations.AddField(
            model_name='post',
            name='published',
            field=models.BooleanField(default=True, verbose_name='Опубликовать?'),
        ),
        migrations.AddField(
            model_name='post',
            name='published_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Дата публикации'),
        ),
        migrations.AddField(
            model_name='post',
            name='sort',
            field=models.PositiveIntegerField(default=0, verbose_name='Порядок'),
        ),
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.BooleanField(default=False, verbose_name='Для зарегистрированных'),
        ),
        migrations.AddField(
            model_name='post',
            name='subtitle',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Под заголовок'),
        ),
        migrations.AddField(
            model_name='post',
            name='template',
            field=models.CharField(default='blog/post_detail.html', max_length=500, verbose_name='Шаблон'),
        ),
        migrations.AddField(
            model_name='post',
            name='viewed',
            field=models.PositiveIntegerField(default=0, verbose_name='Просмотрено'),
        ),
        migrations.AddField(
            model_name='tag',
            name='published',
            field=models.BooleanField(default=True, verbose_name='Отображать?'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата создания'),
        ),
    ]