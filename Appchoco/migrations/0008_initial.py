# Generated by Django 4.1.1 on 2022-09-17 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Appchoco', '0007_delete_productos_delete_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='inicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('fecha', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='productos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('fecha', models.DateField()),
                ('sabor', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('apellido', models.CharField(max_length=60)),
                ('year', models.IntegerField()),
                ('fecha', models.DateField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
