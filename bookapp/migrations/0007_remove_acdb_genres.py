# Generated by Django 4.2 on 2023-05-11 11:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0006_apdb_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='acdb',
            name='genres',
        ),
    ]
