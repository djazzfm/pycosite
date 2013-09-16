from django.contrib import admin
from pycosite.models import Page, PageUrl
from pycosite.forms import PageForm, UrlForm

class UrlInline(admin.TabularInline):
    model = PageUrl
    form = UrlForm
    extra = 1
    max_num = 1
    exclude = ['key']


class PageAdmin(admin.ModelAdmin):
    form = PageForm
    inlines = [UrlInline]
    readonly_fields = ['author', 'date', 'last_editor', 'last_date']
    exclude = ['type', 'format']
    
    def save_model(self, request, obj, form, change):
        if not obj.id:
            obj.author = request.user
        obj.last_editor = request.user
        super(PageAdmin, self).save_model(request, obj, form, change)

admin.site.register(Page, PageAdmin)