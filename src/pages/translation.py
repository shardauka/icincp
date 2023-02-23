from .models import News

from modeltranslation.translator import translator, TranslationOptions

class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'short_description', 'content')

translator.register(News, NewsTranslationOptions)