# Generated by Django 4.2.1 on 2023-05-24 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0010_alter_apdb_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='gndb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('GenreName', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
    ]
