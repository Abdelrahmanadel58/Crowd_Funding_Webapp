# Generated by Django 2.2.11 on 2020-03-18 20:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0003_auto_20200318_2024'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project_tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('prj_tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tproject', to='Project.Projects')),
            ],
        ),
        migrations.CreateModel(
            name='Project_pics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('prj_pic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='oproject', to='Project.Projects')),
            ],
        ),
        migrations.CreateModel(
            name='Project_comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('prj_comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cproject', to='Project.Projects')),
            ],
        ),
        migrations.CreateModel(
            name='comment_reply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reply', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('comment', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='Project.Project_comments')),
            ],
        ),
    ]