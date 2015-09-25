#from django.shortcuts import render
#from .models import entry
from django.views.generic.base import TemplateView
from grab import Grab
class HomePageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        g = Grab()
       # g.setup(url='http://www.kansk-tc.ru/studentam/raspisanie_zanyatij')
        g.go('www.kansk-tc.ru/studentam/raspisanie_zanyatij')
        sait = g.doc.select('//td[@class="inside_center"]').html()
        sait=sait.replace('src="/', 'src="http://www.kansk-tc.ru/')
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['kansk_tc'] = sait
        return context
# Create your views here.
