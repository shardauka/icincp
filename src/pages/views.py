from django.shortcuts import render

from pages.models import News, EOI
from .forms import EOI_Form, HEPoi

def home_view(request, *args, **kwargs):
    context={'news': News.objects.get(id=1)}
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
    context = {'form': form}
    return render(request, 'pages/partner_search.html', context)

def contact_view(request):
    context = {}
    return render(request, 'pages/contact.html', context)

def blog_view(request):
    context = {}
    return render(request, 'pages/blog_type.html', context)