# Generated by Django 4.1 on 2022-08-26 03:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0004_archivos'),
    ]

    operations = [
        migrations.RenameField(
            model_name='archivos',
            old_name='archivo2',
            new_name='archivoExp',
        ),
    ]
