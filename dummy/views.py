from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index_dummy(request):

    return HttpResponse('<h1>This is dummy</h1>')