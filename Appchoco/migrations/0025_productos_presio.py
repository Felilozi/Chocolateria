# Generated by Django 4.1.1 on 2022-09-25 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Appchoco', '0024_remove_productos_presio'),
    ]

    operations = [
        migrations.AddField(
            model_name='productos',
            name='presio',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
