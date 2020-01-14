# Generated by Django 2.2.8 on 2019-12-22 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_remove_emailuser_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailuser',
            name='username',
            field=models.CharField(blank=True, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=50, null=True),
        ),
    ]
