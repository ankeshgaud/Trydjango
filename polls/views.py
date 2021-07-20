from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're hh at thedsada new polls index.")

def test_index(request):
    return HttpResponse("You're at the new pollss ABDBDsba.")
