from django.views.generic import DetailView, ListView
from django.shortcuts import render

from visits.models import Visit, Provider

class VisitList(ListView):
    model = Visit
    template_name = 'visits/visit_list.html'

class VisitDetail(DetailView):
    model = Visit
    template_name = 'visits/visit_detail.html'
