import http
from http.client import HTTPResponse
from django.shortcuts import render

# Create your views here.
def helloview(request):
    return HTTPResponse("Hello World")