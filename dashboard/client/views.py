from django.shortcuts import render
from django.http import HttpResponse


def client(request):
    print("Working")
    return HttpResponse("Working")