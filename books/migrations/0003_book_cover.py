# Generated by Django 3.2.7 on 2021-09-14 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cover',
            field=models.ImageField(blank=True, upload_to='covers/'),
        ),
    ]
