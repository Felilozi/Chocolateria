# Generated by Django 4.1.1 on 2022-09-18 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Appchoco', '0013_contactos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactos',
            name='telefono',
            field=models.CharField(max_length=10),
        ),
    ]
