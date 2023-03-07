from django.shortcuts import render

from pages.models import News
from .forms import EOI_Form

def home_view(request, *args, **kwargs):
    context={'news': News.objects.get(id=1)}
    return render(request, "pages/home.html", context)


def partner_search(request):
    form = EOI_Form()
    if request.method == 'POST':
        print("dsa")
    context = {'form': form}
    return render(request, 'pages/partner_search.html', context)

def contact_view(request):
    context = {}
    return render(request, 'pages/contact.html', context)

def blog_view(request):
    context = {}
    return render(request, 'pages/blog_type.html', context)