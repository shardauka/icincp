from .models import News, GeneralPage

from modeltranslation.translator import translator, TranslationOptions

class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'short_description', 'content')

class GeneralPageTranslationOptions(TranslationOptions):
    fields = ('title', 'content')

translator.register(News, NewsTranslationOptions)
translator.register(GeneralPage, GeneralPageTranslationOptions)