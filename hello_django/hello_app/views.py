from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def print_hello(request):
    return render(request,"main.html")
