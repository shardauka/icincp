from django.contrib import admin
from django.db import models
from .models import News, HEPoi, EOI, GeneralPage, FileStorage, Events, EnrollEvent
from tinymce.widgets import TinyMCE
from django import forms
from django.utils.html import format_html


class NewsAdmin(admin.ModelAdmin):
    list_display  = ['title', 'short_description', 'slug']
    prepopulated_fields = {"slug": ("title",)}
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name in ['content', 'content_ro', 'content_en']:
            kwargs['widget'] = TinyMCE(attrs={'cols': 80, 'rows': 20})
        return super(NewsAdmin, self).formfield_for_dbfield(db_field,**kwargs)


class GeneralPageAdmin(admin.ModelAdmin):
    list_display  = ['title', 'slug']
    prepopulated_fields = {"slug": ("title",)}
    def formfield_for_dbfield(self, db_field, **kwargs): 
        if db_field.name in ['content', 'content_ro', 'content_en']:
            kwargs['widget'] = TinyMCE(attrs={'cols': 80, 'rows': 20})
        if db_field.name in ['short_description', 'short_description_ro', 'short_description_en']:
            kwargs['widget'] = forms.Textarea(attrs={'cols': 80, 'rows': 3})
        return super(GeneralPageAdmin, self).formfield_for_dbfield(db_field,**kwargs)


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
    list_display  = ['name', 'slug', 'file', 'get_absolute_url']


admin.site.register(News, NewsAdmin)
admin.site.register(HEPoi)
admin.site.register(EOI)
admin.site.register(GeneralPage, GeneralPageAdmin)
admin.site.register(FileStorage, FileStorageAdmin)
admin.site.register(Events, EventsAdmin)
admin.site.register(EnrollEvent)