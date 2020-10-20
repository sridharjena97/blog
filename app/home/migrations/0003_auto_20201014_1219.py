# Generated by Django 3.1.2 on 2020-10-14 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20201014_1211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='messageBody',
            field=models.CharField(default='NA', max_length=1000),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='messageTitle',
            field=models.CharField(default='NA', max_length=500),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='mobileNumber',
            field=models.CharField(default='', max_length=13, null=True),
        ),
    ]