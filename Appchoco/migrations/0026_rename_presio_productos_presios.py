# Generated by Django 4.1.1 on 2022-09-25 18:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Appchoco', '0025_productos_presio'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productos',
            old_name='presio',
            new_name='presios',
        ),
    ]
