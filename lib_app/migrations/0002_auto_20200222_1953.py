# Generated by Django 3.0.2 on 2020-02-22 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lib_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='biography',
            field=models.TextField(max_length=5000),
        ),
    ]
