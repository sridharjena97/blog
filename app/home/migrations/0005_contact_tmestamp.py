# Generated by Django 3.1.2 on 2020-10-14 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20201014_1230'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='tmeStamp',
            field=models.TimeField(auto_now=True),
        ),
    ]