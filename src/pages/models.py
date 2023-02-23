from django.db import models
from django.utils.translation import gettext_lazy as _

import datetime


class News(models.Model):
    title = models.CharField(max_length = 64, help_text=_('News title'))
    short_description = models.CharField(max_length = 256, blank=True, null=True, help_text=_('Short description'))
    content = models.CharField(max_length = 2048, blank=True, null=True, help_text=_('Content'))
    date_published = models.DateTimeField(default=datetime.datetime.now, help_text=_('Published date'))
    
    class Meta():
        verbose_name = ('News')
        verbose_name_plural = ('News')

