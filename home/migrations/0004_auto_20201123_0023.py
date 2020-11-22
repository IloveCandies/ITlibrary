# Generated by Django 3.0.8 on 2020-11-22 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_book'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='file',
        ),
        migrations.AddField(
            model_name='book',
            name='source',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
