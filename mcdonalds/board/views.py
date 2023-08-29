from datetime import datetime, timedelta

from django.http import HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .tasks import hello, printer

class IndexView(LoginRequiredMixin,TemplateView):
    template_name = 'protect/index.html'

    def get(self, request):
        printer.apply_async([10],
                            ta = datetime.now() + timedelta(seconds=5))
        hello.delay()
        return HttpResponse('Hello!')


