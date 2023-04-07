"""icincp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from pages.views import home_view, partner_search, contact_view, blog_view, general_page_view, news_detail_view, news_page_view, storagefile_view, thank_you_view
from django.conf.urls.i18n import i18n_patterns


admin.site.site_header = 'NCP-ICI Admin Panel'


urlpatterns = [
    path(r'^i18n/', include('django.conf.urls.i18n')),
    #path('admin/', admin.site.urls),
    #path('', home_view, name="home"),
    #path('i18n/', include('django.conf.urls.i18n')),
    path('storage/<slug:slug>/', storagefile_view, name='filestorage'),
]

urlpatterns += i18n_patterns(
    path('tinymce/', include('tinymce.urls')),
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('partnersearch', partner_search, name='partnersearch'),
    path('thank_you', thank_you_view, name='form_submit_thank_you'),
    path('contact', contact_view, name='contact'),
    path('blogpage', blog_view, name='blogpage'),
    path('news/', news_page_view, name='news'),
    path('news-detail/<slug:slug>/', news_detail_view, name='news_detail'),
    path('<slug:slug>/', general_page_view, name='contentpage'),
    
    

    
)
