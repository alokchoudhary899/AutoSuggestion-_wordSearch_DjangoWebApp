from __future__ import absolute_import
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views.generic import TemplateView
import json
from django.db.models.functions import Length
from searchApp.models import SearchElements


class IndexView(LoginRequiredMixin,TemplateView):
    template_name = 'index.html'

def wordAutocomplete(request):
    if request.is_ajax():
        q = request.GET.get('term', '').capitalize()
        search_qs = SearchElements.objects.values().order_by(Length('words').asc(),'-Use_count').filter(words__icontains=q)[:24]
        results = []
        print(q)
        for r in search_qs:
            results.append(r['words'])
        data = json.dumps(results)
    else:
        q = request.POST.get('txtSearch')
        search_qs = SearchElements.objects.values().order_by(Length('words').asc(),'-Use_count').filter(words__icontains=q)[:24]
        results = []
        print(q)
        for r in search_qs:
            results.append('word : '+str(r['words'])+'||'+'use count : '+str(r['Use_count']))
        data = json.dumps(results)
    datatype = 'application/json'
    return HttpResponse(data, datatype)
