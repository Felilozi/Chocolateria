# Generated by Django 4.1.1 on 2022-09-25 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Appchoco', '0015_productos_idp'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactos',
            old_name='instagram',
            new_name='nombre',
        ),
        migrations.AddField(
            model_name='contactos',
            name='mensaje',
            field=models.CharField(default='nombre', max_length=250),
            preserve_default=False,
        ),
    ]
