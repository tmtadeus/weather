# Generated by Django 4.0.6 on 2022-08-02 17:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weatherapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userinfo',
            options={'verbose_name': 'User info', 'verbose_name_plural': 'Users info'},
        ),
    ]
