# Generated by Django 4.2.5 on 2023-10-02 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0007_alter_news_options_alter_news_author_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='like_count',
            field=models.IntegerField(blank=True, default=0, editable=False, null=True),
        ),
    ]
