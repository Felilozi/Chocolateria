# Generated by Django 4.1.1 on 2022-09-17 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Appchoco', '0012_delete_inicio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contactos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefono', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('instagram', models.CharField(max_length=60)),
            ],
        ),
    ]