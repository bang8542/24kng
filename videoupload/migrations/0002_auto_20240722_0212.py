# Generated by Django 3.2 on 2024-07-22 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videoupload', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='thumbnails/'),
        ),
        migrations.AlterField(
            model_name='video',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='videos/'),
        ),
    ]
