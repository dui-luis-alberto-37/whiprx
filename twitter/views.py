from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponseRedirect, HttpResponse
from twitter.models import TwitterAccount

# Create your views here.
class MyView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Hello, World!, im Dui")
