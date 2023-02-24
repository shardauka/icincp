from django.shortcuts import render

from pages.models import News

def home_view(request, *args, **kwargs):
    context={'news': News.objects.get(id=1)}
    return render(request, "pages/home.html", context)


def partner_search(request):
    context = {}
    return render(request, 'pages/partner_search.html', context)