from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the new polls index.")

def test_index(request):
    return HttpResponse("Hello, world. You're at the new polls indessx.")
