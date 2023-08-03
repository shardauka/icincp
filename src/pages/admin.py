from django.contrib import admin
from django.db import models
from .models import News, HEPoi, EOI, GeneralPage, FileStorage, Events, EnrollEvent
from tinymce.widgets import TinyMCE
from django import forms
from django.utils.html import format_html
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

class NewsAdmin(admin.ModelAdmin):
    list_display  = ['title', 'short_description', 'slug']
    prepopulated_fields = {"slug": ("title",)}
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name in ['content', 'content_ro', 'content_en']:
            kwargs['widget'] = TinyMCE(attrs={'cols': 80, 'rows': 20})
        return super(NewsAdmin, self).formfield_for_dbfield(db_field,**kwargs)


class GeneralPageAdmin(admin.ModelAdmin):
    list_display  = ['title', 'custom_absolute_url']
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ['title', 'content', 'content_en', 'content_ro']
    def formfield_for_dbfield(self, db_field, **kwargs): 
        if db_field.name in ['content', 'content_ro', 'content_en']:
            kwargs['widget'] = TinyMCE(attrs={'cols': 80, 'rows': 20})
        if db_field.name in ['short_description', 'short_description_ro', 'short_description_en']:
            kwargs['widget'] = forms.Textarea(attrs={'cols': 80, 'rows': 3})
        return super(GeneralPageAdmin, self).formfield_for_dbfield(db_field,**kwargs)

    def get_absolute_url(self, obj):
        return reverse('filestorage', kwargs={'slug': obj.slug})
    
    def custom_absolute_url(self, obj):
        if obj.pk:
            return format_html('<a href="{url}" target="_blank">{url}</a>'.format(url=obj.get_absolute_url()))
        return _('File does not exist')
    custom_absolute_url.short_description = _('Page URL')


class EventsAdmin(admin.ModelAdmin):
    list_display  = ['title', 'short_description', 'slug', 'expired']
    prepopulated_fields = {"slug": ("title",)}
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name in ['content', 'content_ro', 'content_en']:
            kwargs['widget'] = TinyMCE(attrs={'cols': 80, 'rows': 20})
        if db_field.name in ['short_description', 'short_description_ro', 'short_description_en']:
            kwargs['widget'] = forms.Textarea(attrs={'cols': 80, 'rows': 3})
        return super(EventsAdmin, self).formfield_for_dbfield(db_field,**kwargs)
    
    def expired(self, obj):
        if obj.is_expired():
            return format_html('<div style="color: red; font-weight: bold;">%s</div>' % obj.is_expired())
        return format_html('<div style="color: green; font-weight: bold;">%s</div>' % obj.is_expired())
    
    

class FileStorageAdmin(admin.ModelAdmin):
    list_display  = ['name', 'slug', 'file', 'custom_absolute_url']
    prepopulated_fields = {"slug": ("name",)}
    readonly_fields = ['custom_absolute_url']

    def get_absolute_url(self, obj):
        return reverse('filestorage', kwargs={'slug': obj.slug})
    
    def custom_absolute_url(self, obj):
        if obj.pk:
            return format_html('<a href="{url}" target="_blank">{url}</a>'.format(url=obj.get_absolute_url()))
        return _('File does not exist')
    
    custom_absolute_url.short_description = _('File URL')
    #get_absolute_url.allow_tags = True

admin.site.register(News, NewsAdmin)
admin.site.register(HEPoi)
admin.site.register(EOI)
admin.site.register(GeneralPage, GeneralPageAdmin)
admin.site.register(FileStorage, FileStorageAdmin)
admin.site.register(Events, EventsAdmin)
admin.site.register(EnrollEvent)