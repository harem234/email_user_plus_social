# Generated by Django 2.2.8 on 2019-12-22 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_auto_20191223_0012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailuser',
            name='email',
            field=models.EmailField(error_messages={'unique': 'A user with that email already exists.'}, max_length=254, unique=True, verbose_name='email address'),
        ),
    ]
