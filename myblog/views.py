from django.http import HttpResponse
from django.shortcuts import render,redirect



def home(request):
    return redirect('/articles/')


def about(request):
    return render(request,'about.html')
