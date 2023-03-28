from django.db import models
from django.utils.translation import gettext_lazy as _
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.urls import reverse

import datetime


class News(models.Model):
    title = models.CharField(max_length = 64, help_text=_('News title'))
    slug = models.SlugField(unique=True, help_text=_('URL address of the news detail page'))
    short_description = models.CharField(max_length = 256, blank=True, null=True, help_text=_('Short description'))
    content = models.CharField(max_length = 2048, blank=True, null=True, help_text=_('Content'))
    date_published = models.DateTimeField(default=datetime.datetime.now, help_text=_('Published date'))
    
    
    class Meta():
        verbose_name = _('News')
        verbose_name_plural = _('News')
    
    def get_absolute_url(self):
        return reverse('news_detail', kwargs={'slug': self.slug})
    
    def get_lates_news():
        return News.objects.all().order_by("-id")[0:3]



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
    

    def send_email(self):
        plaintext = get_template('email/eoi_mail.txt')
        htmly     = get_template('email/eoi_mail.html')
        d = { 'eoi': self}
        subject, from_email, to = 'Expression of interest', 'no-reply@ici.ro', 'mihai.apostol@ici.ro'
        text_content = plaintext.render(d)
        html_content = htmly.render(d)
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        return 0
    


class GeneralPage(models.Model):
    title = models.CharField(max_length = 64, help_text=_('News title'))
    slug = models.SlugField(unique=True, help_text=_('URL address of the page'))
    content = models.TextField(blank=True, null=True, help_text=_('Content'))

    class Meta:
        verbose_name = _('General page')
        verbose_name_plural = _('General pages')
    
    def get_absolute_url(self):
        return reverse('contentpage', kwargs={'slug': self.slug})
    

class FileStorage(models.Model):
    file = models.FileField()
    name = models.CharField(max_length = 64, help_text=_('File name'))
    slug = models.SlugField(unique=True, help_text=_('URL address of the file'))

    class Meta:
        verbose_name = _('File storage')
        verbose_name_plural = _('Files storage')

    def get_absolute_url(self):
        return reverse('filestorage', kwargs={'slug': self.slug})