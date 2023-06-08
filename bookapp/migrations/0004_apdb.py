# Generated by Django 4.2 on 2023-04-19 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0003_acdb_genres'),
    ]

    operations = [
        migrations.CreateModel(
            name='apdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=30, null=True)),
                ('Categoryname', models.CharField(blank=True, max_length=30, null=True)),
                ('Genres', models.CharField(blank=True, max_length=30, null=True)),
                ('Price', models.IntegerField(blank=True, max_length=30, null=True)),
                ('Page', models.IntegerField(blank=True, max_length=30, null=True)),
                ('About', models.CharField(blank=True, max_length=30, null=True)),
                ('Imagee', models.ImageField(blank=True, null=True, upload_to='profile')),
            ],
        ),
    ]
