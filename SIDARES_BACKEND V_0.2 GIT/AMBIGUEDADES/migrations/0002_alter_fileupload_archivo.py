# Generated by Django 4.0.5 on 2022-07-29 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AMBIGUEDADES', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fileupload',
            name='archivo',
            field=models.FileField(blank=True, default='SOME STRING', upload_to='archivos/'),
        ),
    ]