# Generated by Django 4.1.7 on 2023-03-07 10:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_alter_news_options_news_content_en_news_content_ro_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='HEPoi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Horizon Europe programm of interest', max_length=64)),
                ('description', models.CharField(blank=True, help_text='Horizon Europe programm description', max_length=512, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EOI',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text='First name', max_length=32)),
                ('last_name', models.CharField(help_text='Last name', max_length=32)),
                ('email', models.EmailField(help_text='Email address', max_length=254)),
                ('organization_pozition', models.CharField(help_text='Organization pozition', max_length=64)),
                ('organization_name', models.CharField(help_text='Organization name', max_length=64)),
                ('organization_acronym', models.CharField(help_text='Organization acronym', max_length=16)),
                ('organization_short_description', models.CharField(help_text='Organization short description', max_length=1024)),
                ('research_fields', models.CharField(help_text='Research fields', max_length=256)),
                ('key_words', models.CharField(help_text='Key words', max_length=512)),
                ('department_short_description', models.CharField(help_text='Department short description', max_length=2048)),
                ('skills_competences', models.CharField(help_text='Skills and competences', max_length=1024)),
                ('scientific_publication', models.CharField(help_text='Scientific publications', max_length=2048)),
                ('related_projects', models.CharField(help_text='Related projects', max_length=2048)),
                ('achievements', models.CharField(help_text='Department short description', max_length=2048)),
                ('other', models.CharField(help_text='Other information', max_length=1024)),
                ('hepoi', models.ForeignKey(help_text='programm of interest', on_delete=django.db.models.deletion.CASCADE, to='pages.hepoi')),
            ],
            options={
                'verbose_name': 'EOI',
                'verbose_name_plural': 'EOIs',
            },
        ),
    ]
