# from django.shortcuts import render
# from django.views import View
from django.views.generic import TemplateView


# def index(request):
#     return render(request, 'index.html')

class Indexviews(TemplateView):
   template_name = 'index.html'