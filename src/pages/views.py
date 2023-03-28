from django.shortcuts import render, redirect, get_object_or_404

from pages.models import News, EOI, GeneralPage, FileStorage
from .forms import EOI_Form, HEPoi
import os
from django.http import HttpResponse



def home_view(request, *args, **kwargs):
    context={'news': News.get_lates_news}
    return render(request, "pages/home.html", context)


def partner_search(request):
    form = EOI_Form()
    if request.method == 'POST':
        form = EOI_Form(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            #separating hepoi from form data because manytomany field
            hepoi = cleaned_data['hepoi']
            cleaned_data.pop('hepoi')
            eoi = EOI.objects.create(**cleaned_data)
            for i in hepoi:
                eoi.hepoi.add(i)
            eoi.save()
            eoi.send_email()
    context = {'form': form}
    return render(request, 'pages/partner_search.html', context)

def contact_view(request):
    context = {}
    return render(request, 'pages/contact.html', context)

def blog_view(request):
    context = {}
    return render(request, 'pages/blog_type.html', context)

def general_page_view(request, slug):
    page = GeneralPage.objects.get(slug=slug)
    print(page.get_absolute_url())
    context = {'page': page}
    return render(request, 'pages/general_page.html', context)


def news_page_view(request):
    news = News.objects.all()
    context = {'news': news}
    return render(request, 'pages/news.html', context)

def news_detail_view(request, slug):
    news_detail = News.objects.get(slug=slug)
    context = {'news': news_detail}
    return render(request, 'pages/news_detail.html', context)

def storagefile_view(request, slug):
    file = FileStorage.objects.get(slug=slug)
    ext = os.path.splitext(file.file.path)[1].replace('.', '')
    if ext in ['pdf']:
        content_type = 'application/' + ext
    else:
        content_type = 'image/' + ext
    response = HttpResponse(file.file, content_type=content_type)
    response['Content-Disposition'] = 'filename='+file.file.name
    return response