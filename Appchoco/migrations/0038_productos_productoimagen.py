# Generated by Django 4.1.1 on 2022-10-07 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Appchoco', '0037_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='productos',
            name='productoImagen',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
