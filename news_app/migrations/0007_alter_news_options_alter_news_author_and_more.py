# Generated by Django 4.2.5 on 2023-10-02 12:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news_app', '0006_newsdetails'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
        migrations.AlterField(
            model_name='news',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='news',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='news',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='news',
            name='main_image',
            field=models.ImageField(upload_to='', verbose_name='Главное имя'),
        ),
        migrations.AlterField(
            model_name='news',
            name='text',
            field=models.TextField(verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(max_length=250, verbose_name='Жизнь в городе'),
        ),
    ]
