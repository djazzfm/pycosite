from django.shortcuts import render
from django.http import HttpResponseNotFound
from django.template import loader, RequestContext
from pycosite.models import Page


def page_unavailable(request, url):
    tpl_name = 'pycosite/responses/HttpResponseNotFound.html'
    t = loader.get_template(tpl_name)
    c = RequestContext(request, {})
    c['url'] = url
    return HttpResponseNotFound(t.render(c))

def view(request, url):
    try:
        p = Page.objects.get_from_url(url)
        if p.status == 'published':
            return render(request,
                          'pycosite/layouts/%s' % p.get_layout(),
                          {'page': p})
        else:
            return page_unavailable(request, url)
    
    except Page.DoesNotExist:
        return page_unavailable(request, url)
