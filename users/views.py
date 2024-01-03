from django.shortcuts import render
from django.http import HttpResponse

def register(request):
    return HttpResponse("User register page.")

def login(request):
    return HttpResponse("User login page.")