from django import forms
from pycosite.models import Page, PageUrl


STATUS_CHOICES = (('offline', 'offline'),
                  ('published', 'published'))


class PageForm(forms.ModelForm):
    status = forms.ChoiceField(choices=STATUS_CHOICES)
    class Meta:
        model = Page

class UrlForm(forms.ModelForm):
    class Meta:
        model = PageUrl
