# Generated by Django 2.2.11 on 2020-03-23 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0012_auto_20200323_1711'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='Nor',
            field=models.IntegerField(default=0),
        ),
    ]
