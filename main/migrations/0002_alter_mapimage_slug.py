# Generated by Django 4.0.2 on 2022-02-21 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mapimage',
            name='slug',
            field=models.SlugField(max_length=255, verbose_name='slug'),
        ),
    ]