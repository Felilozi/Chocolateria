# Generated by Django 4.1.1 on 2022-10-02 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Appchoco', '0035_delete_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('apellido', models.CharField(max_length=60)),
                ('fecha', models.DateField()),
                ('year', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.DeleteModel(
            name='Contraseña',
        ),
    ]
