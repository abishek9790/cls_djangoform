from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import FormView
from app.forms import *

# Create your views here.
class cbv_djangoform(FormView):
    template_name='cbv_djangoform.html'
    form_class=emp

    def form_valid(self, form):
        data=form.cleaned_data
        return HttpResponse(str(data))