from djazz.models import Post, PostManager, PostVar, PostVarManager
from django.db import IntegrityError


class PageManager(PostManager):
    POST_TYPE = 'pycopage'
    
    def get_from_url(self, url):
        p = Page.objects.get(postvar__key='url', postvar__value=url)
        return p

class Page(Post):
    
    objects = PageManager()
    
    class Meta:
        proxy = True
    
    def get_url(self):
        return self.postvar.get(key='url').value
    
    def set_url(self, url):
        if PageUrl.objects.filter(value=url)\
                          .exclude(post=self)\
                          .count() > 0:
            raise IntegrityError("url %s already exists" % url)
        
        o, c = self.postvar.get_or_create(key='url')
        o.value = url
        o.save()
    
    def get_layout(self):
        try:
            return self.postvar.get(key='layout').value
        except PostVar.DoesNotExist:
            return 'default.html'
    
    def set_layout(self, layout):
        o, c = self.postvar.get_or_create(key='layout')
        o.value = layout
        o.save()
    
    def save(self, *args, **kwargs):
        from django.utils import timezone
        if not self.id:
            self.date = timezone.now()
        self.last_date = timezone.now()
        return super(Page, self).save(*args, **kwargs)


class UrlManager(PostVarManager):
    VAR_TYPE = 'url'

class PageUrl(PostVar):
    objects = UrlManager()
    
    class Meta:
        proxy = True
