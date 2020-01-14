# Generated by Django 2.2.7 on 2019-11-13 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0006_auto_20191113_0232'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='socialaccount',
            constraint=models.UniqueConstraint(fields=('social_id', 'provider', 'site'), name='every social_id  per provider is unique for every site'),
        ),
    ]
