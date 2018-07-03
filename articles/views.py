from django.shortcuts import render
from .models import Article
from django.http import HttpResponse

# Create your views here.
def article_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request,'articles/article_list.html',{'articles':articles})

def article_deatail(request,slug):

    article = Article.objects.get(slug = slug)

    return render(request,'articles/article_deatail.html', {'article':article} )
def article_create(request):
    return HttpResponse('create page')
