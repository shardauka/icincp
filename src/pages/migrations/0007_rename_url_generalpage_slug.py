# Generated by Django 4.1.7 on 2023-03-13 11:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_alter_generalpage_options_alter_generalpage_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='generalpage',
            old_name='url',
            new_name='slug',
        ),
    ]
