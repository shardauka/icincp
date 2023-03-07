from django.db import models
from django.utils.translation import gettext_lazy as _

import datetime


class News(models.Model):
    title = models.CharField(max_length = 64, help_text=_('News title'))
    short_description = models.CharField(max_length = 256, blank=True, null=True, help_text=_('Short description'))
    content = models.CharField(max_length = 2048, blank=True, null=True, help_text=_('Content'))
    date_published = models.DateTimeField(default=datetime.datetime.now, help_text=_('Published date'))
    
    class Meta():
        verbose_name = _('News')
        verbose_name_plural = _('News')


class HEPoi(models.Model):
    name = models.CharField(max_length = 64, help_text=_('Horizon Europe programm of interest'))
    description = models.CharField(max_length = 512, help_text=_('Horizon Europe programm description'), blank=True, null=True)

    def __str__(self) -> str:
        return self.name

class EOI(models.Model):
    first_name = models.CharField(max_length = 32, help_text=_('First name'))
    last_name = models.CharField(max_length = 32, help_text=_('Last name'))
    email = models.EmailField(help_text=_('Email address'))
    organization_pozition = models.CharField(max_length = 64, help_text=_('Organization pozition'))
    organization_name = models.CharField(max_length = 64, help_text=_('Organization name'))
    organization_acronym = models.CharField(max_length = 16, help_text=_('Organization acronym'))
    organization_short_description = models.CharField(max_length = 1024, help_text=_('Organization short description'))
    research_fields = models.CharField(max_length = 256, help_text=_('Research fields'))
    key_words = models.CharField(max_length = 512, help_text=_('Key words'))
    hepoi = models.ManyToManyField(HEPoi, help_text=_('programm of interest'))
    department_short_description = models.CharField(max_length = 2048, help_text=_('Department short description'))
    skills_competences = models.CharField(max_length = 1024, help_text=_('Skills and competences'))
    scientific_publication = models.CharField(max_length = 2048, help_text=_('Scientific publications'))
    related_projects = models.CharField(max_length = 2048, help_text=_('Related projects'))
    achievements = models.CharField(max_length = 2048, help_text=_('Department short description'))
    other = models.CharField(max_length = 1024, help_text=_('Other information'))

    class Meta:
        verbose_name = _('EOI')
        verbose_name_plural = _('EOIs')

    def __str__(self) -> str:
        return self.email + ' ' + self.first_name + ' ' + self.last_name
    