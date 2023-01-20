from django.urls import reverse_lazy, reverse
from django.utils.text import capfirst
from django.utils.translation import gettext, gettext_lazy as _
from django.views.generic.list import ListView
from django.views.generic.edit import FormMixin
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages

from pagebuilders.mixins import ContextTitleMixin
from pagebuilders.models import Page


@method_decorator(login_required, name="dispatch")
class PageListView(ContextTitleMixin, ListView):
    model = Page
    title_page = "Page List"
    

    def get_queryset(self):
        search = self.request.GET.get("search")
        if search:
            object_list = self.model.objects.filter(title__icontains=search)
        else:
            object_list = self.model.objects.all()
        return object_list
          

    def get_context_data(self, **kwargs):
        page_number = self.request.GET.get('page', 1)
        context = super().get_context_data(**kwargs)
        return context
    
    

