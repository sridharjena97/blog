# Generated by Django 3.1.2 on 2020-10-14 06:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contacts',
            old_name='mesaageTitle',
            new_name='messageTitle',
        ),
    ]