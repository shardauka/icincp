# Generated by Django 4.1.7 on 2023-03-13 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_generalpage'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='generalpage',
            options={'verbose_name': 'General page', 'verbose_name_plural': 'General pages'},
        ),
        migrations.AlterField(
            model_name='generalpage',
            name='url',
            field=models.SlugField(help_text='URL address of the page', unique=True),
        ),
    ]
