# Generated by Django 4.2.1 on 2023-05-25 10:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0003_rename_cartdb_carttdb'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carttdb',
            name='productimagee',
        ),
        migrations.RemoveField(
            model_name='carttdb',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='carttdb',
            name='totalproduct',
        ),
    ]