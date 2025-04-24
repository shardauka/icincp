from django.contrib import admin
from .models import News, HEPoi, EOI, GeneralPage, FileStorage, Events, EnrollEvent
from tinymce.widgets import TinyMCE
from django import forms
from django.utils.html import format_html
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
import os

class NewsAdmin(admin.ModelAdmin):
    list_display  = ['title', 'short_description', 'slug']
    prepopulated_fields = {"slug": ("title_en",)}
    exclude = ['title','content', 'short_description']
    readonly_fields = ['date_published']
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name in ['content_ro', 'content_en']:
            kwargs['widget'] = TinyMCE(attrs={'cols': 80, 'rows': 20})
        if db_field.name in ['short_description_ro', 'short_description_en']:
            kwargs['widget'] = forms.Textarea(attrs={'cols': 80, 'rows': 3})
        return super(NewsAdmin, self).formfield_for_dbfield(db_field,**kwargs)
    
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['title_ro'].required = True
        form.base_fields['title_en'].required = True
        form.base_fields['short_description_ro'].required = True
        form.base_fields['short_description_en'].required = True
        return form


class GeneralPageAdmin(admin.ModelAdmin):
    list_display  = ['title', 'custom_absolute_url']
    prepopulated_fields = {"slug": ("title_en",)}
    search_fields = ['content_en', 'content_ro']
    exclude = ['title', 'content']
    def formfield_for_dbfield(self, db_field, **kwargs): 
        if db_field.name in ['content_ro', 'content_en']:
            kwargs['widget'] = TinyMCE(attrs={'cols': 80, 'rows': 20})
        if db_field.name in ['short_description_ro', 'short_description_en']:
            kwargs['widget'] = forms.Textarea(attrs={'cols': 80, 'rows': 3})
        return super(GeneralPageAdmin, self).formfield_for_dbfield(db_field,**kwargs)

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['title_ro'].required = True
        form.base_fields['title_en'].required = True
        return form

    def get_absolute_url(self, obj):
        return reverse('filestorage', kwargs={'slug': obj.slug})
    
    def custom_absolute_url(self, obj):
        if obj.pk:
            return format_html('<a href="{url}" target="_blank">{url}</a>'.format(url=obj.get_absolute_url()))
        return _('File does not exist')
    custom_absolute_url.short_description = _('Page URL')


class EventsAdmin(admin.ModelAdmin):
    list_display  = ['title', 'short_description', 'slug', 'expired']
    prepopulated_fields = {"slug": ("title_en",)}
    exclude = ['title','content', 'short_description']
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name in ['content_ro', 'content_en']:
            kwargs['widget'] = TinyMCE(attrs={'cols': 80, 'rows': 20})
        if db_field.name in ['short_description_ro', 'short_description_en']:
            kwargs['widget'] = forms.Textarea(attrs={'cols': 80, 'rows': 3})
        return super(EventsAdmin, self).formfield_for_dbfield(db_field,**kwargs)
    
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['title_ro'].required = True
        form.base_fields['title_en'].required = True
        form.base_fields['short_description_ro'].required = True
        form.base_fields['short_description_en'].required = True
        return form

    def expired(self, obj):
        if obj.is_expired():
            return format_html('<div style="color: red; font-weight: bold;">%s</div>' % obj.is_expired())
        return format_html('<div style="color: green; font-weight: bold;">%s</div>' % obj.is_expired())
    
    

class FileStorageAdmin(admin.ModelAdmin):
    list_display  = ['name', 'slug', 'file', 'custom_absolute_url']
    prepopulated_fields = {"slug": ("name",)}
    readonly_fields = ['custom_absolute_url', 'img_preview']

    def get_absolute_url(self, obj):
        return reverse('filestorage', kwargs={'slug': obj.slug})
    
    def custom_absolute_url(self, obj):
        if obj.pk:
            return format_html('<a href="{url}" target="_blank">{url}</a>'.format(url=obj.get_absolute_url()))
        return _('File does not exist')
    custom_absolute_url.short_description = _('File URL')

    def img_preview(self, obj):
        if obj.file:
            file_extension = os.path.splitext(obj.file.name)[1].lower()
            image_extensions = ['.jpg', '.jpeg', '.png', '.gif']
            if file_extension in image_extensions:
                return format_html(f'<img src="{obj.file.url}" width="300"/>')
        return _('No image preview available')
    img_preview.short_description = _('Image preview')
    
    # def save_model(self, request, obj, form, change):
    #     if not obj.slug:  # Only prepopulate if the slug is empty
    #         slug_value = f"{obj.name}-{obj.id}"  # Use a combination of name and id for the slug
    #         obj.slug = slug_value.replace(" ", "-")  # Prepopulate the slug (replace spaces with dashes)
    #     super().save_model(request, obj, form, change)



admin.site.register(News, NewsAdmin)
admin.site.register(HEPoi)
admin.site.register(EOI)
admin.site.register(GeneralPage, GeneralPageAdmin)
admin.site.register(FileStorage, FileStorageAdmin)
admin.site.register(Events, EventsAdmin)
admin.site.register(EnrollEvent)