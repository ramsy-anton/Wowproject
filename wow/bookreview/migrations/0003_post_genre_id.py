# Generated by Django 4.0 on 2021-12-18 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookreview', '0002_auto_20211214_1508'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='genre_id',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
