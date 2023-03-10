from django.contrib import admin
from django.db import models
from .models import News, HEPoi, EOI, GeneralPage
from tinymce.widgets import TinyMCE


class NewsAdmin(admin.ModelAdmin):
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name in ['content', 'content_ro', 'content_en']:
            kwargs['widget'] = TinyMCE(attrs={'cols': 80, 'rows': 20})
        return super(NewsAdmin, self).formfield_for_dbfield(db_field,**kwargs)


class GeneralPageAdmin(admin.ModelAdmin):
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name in ['content', 'content_ro', 'content_en']:
            kwargs['widget'] = TinyMCE(attrs={'cols': 80, 'rows': 20})
        return super(GeneralPageAdmin, self).formfield_for_dbfield(db_field,**kwargs)


admin.site.register(News, NewsAdmin)
admin.site.register(HEPoi)
admin.site.register(EOI)
admin.site.register(GeneralPage, GeneralPageAdmin)