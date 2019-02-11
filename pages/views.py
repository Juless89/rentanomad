from django.shortcuts import render
from django.views.generic import View

# Create your views here.
class WordpressPageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')

class DjangoPageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'django.html')