# Generated by Django 4.0.5 on 2022-09-13 18:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AMBIGUEDADES', '0003_file_delete_fileupload'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='classification',
        ),
        migrations.RemoveField(
            model_name='file',
            name='datetime',
        ),
        migrations.RemoveField(
            model_name='file',
            name='status',
        ),
    ]
