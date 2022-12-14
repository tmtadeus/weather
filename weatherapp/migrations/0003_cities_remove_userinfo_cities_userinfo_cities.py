# Generated by Django 4.0.6 on 2022-08-03 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weatherapp', '0002_alter_userinfo_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='cities',
        ),
        migrations.AddField(
            model_name='userinfo',
            name='cities',
            field=models.ManyToManyField(to='weatherapp.cities'),
        ),
    ]
