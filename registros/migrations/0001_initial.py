# Generated by Django 4.1 on 2022-08-25 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cabaña',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='Clave')),
                ('nombre', models.CharField(max_length=50)),
                ('costoDia', models.IntegerField(verbose_name='Costo por día')),
                ('NumPer', models.IntegerField(verbose_name='Número de personas')),
                ('NumCamas', models.IntegerField(verbose_name='Número de camas')),
                ('Servicios', models.TextField()),
                ('Ubicacion', models.CharField(max_length=50)),
                ('oferta', models.CharField(max_length=50)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='fotos')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Cabaña',
                'verbose_name_plural': 'Cabañas',
                'ordering': ['id'],
            },
        ),
    ]
