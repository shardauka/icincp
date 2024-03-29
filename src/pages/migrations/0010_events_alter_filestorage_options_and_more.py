# Generated by Django 4.1.7 on 2023-03-30 10:28

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0009_filestorage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='News title', max_length=64)),
                ('slug', models.SlugField(help_text='URL address of the event detail page', unique=True)),
                ('short_description', models.CharField(blank=True, help_text='Short description', max_length=256, null=True)),
                ('content', models.CharField(blank=True, help_text='Content', max_length=2048, null=True)),
                ('date_published', models.DateTimeField(default=datetime.datetime.now, help_text='Published date')),
                ('date_start', models.DateTimeField(default=datetime.datetime.now, help_text='Start date')),
                ('date_end', models.DateTimeField(default=datetime.datetime.now, help_text='End date')),
            ],
            options={
                'verbose_name': 'Event',
                'verbose_name_plural': 'Events',
            },
        ),
        migrations.AlterModelOptions(
            name='filestorage',
            options={'verbose_name': 'File storage', 'verbose_name_plural': 'Files storage'},
        ),
        migrations.AlterField(
            model_name='filestorage',
            name='file',
            field=models.FileField(upload_to=''),
        ),
        migrations.CreateModel(
            name='EnrollEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text='First name', max_length=32)),
                ('last_name', models.CharField(help_text='Last name', max_length=32)),
                ('email', models.EmailField(max_length=254)),
                ('telephone', models.CharField(help_text='Telephone', max_length=13)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.events')),
            ],
        ),
    ]
