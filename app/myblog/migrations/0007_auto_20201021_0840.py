# Generated by Django 3.1.2 on 2020-10-21 03:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0006_auto_20201019_1328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(default='site admin', on_delete=django.db.models.deletion.SET_DEFAULT, to='myblog.category'),
        ),
    ]
