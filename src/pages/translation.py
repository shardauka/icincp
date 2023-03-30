from .models import News, GeneralPage, Events

from modeltranslation.translator import translator, TranslationOptions

class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'short_description', 'content')

class GeneralPageTranslationOptions(TranslationOptions):
    fields = ('title', 'content')

class EventTranslationOptions(TranslationOptions):
    fields = ('title', 'short_description', 'content')

translator.register(News, NewsTranslationOptions)
translator.register(GeneralPage, GeneralPageTranslationOptions)
translator.register(Events, EventTranslationOptions)