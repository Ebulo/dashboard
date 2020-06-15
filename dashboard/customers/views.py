from django.shortcuts import render
from django.http import HttpResponse


def customers(request):
    print("costumers")
    return HttpResponse("costumers")