# Generated by Django 4.0.5 on 2022-09-19 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AMBIGUEDADES', '0008_alter_ambiguedad_requisito'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ambiguedad',
            name='descripcion',
            field=models.TextField(default='', max_length=5000),
        ),
        migrations.AlterField(
            model_name='ambiguedad',
            name='tipo',
            field=models.CharField(default='', max_length=5000),
        ),
    ]