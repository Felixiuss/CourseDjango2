# Generated by Django 2.2.7 on 2020-04-10 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200329_1913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='tag', to='blog.Tag', verbose_name='Тег'),
        ),
    ]
