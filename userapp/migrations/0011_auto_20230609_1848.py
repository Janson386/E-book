# Generated by Django 3.2.10 on 2023-06-09 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0010_remove_carttdb_pdf'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='book',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='cart',
        ),
        migrations.AddField(
            model_name='carttdb',
            name='pdf',
            field=models.FileField(blank=True, null=True, upload_to='document'),
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='CartItem',
        ),
    ]
