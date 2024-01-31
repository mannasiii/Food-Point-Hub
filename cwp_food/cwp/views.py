# from django.shortcuts import render
from django.http import HttpResponse

def my_view(request):
    msg = "codeswithpankaj.com"
    return HttpResponse(msg)


def web(request):
    msg = "p4n"
    return HttpResponse(msg)
