# Generated by Django 4.1.1 on 2022-09-21 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Appchoco', '0014_alter_contactos_telefono'),
    ]

    operations = [
        migrations.AddField(
            model_name='productos',
            name='idP',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
