# Generated by Django 3.1.1 on 2020-10-19 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(blank=True, choices=[('tech', 'TECHNOLOGY'), ('py', 'PYTHON'), ('js', 'JAVA SCRIPT')], max_length=10),
        ),
    ]