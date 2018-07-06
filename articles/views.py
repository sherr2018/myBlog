from django.shortcuts import render,redirect
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import CreareArticle
# Create your views here.
def article_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request,'articles/article_list.html',{'articles':articles})

def article_detail(request,slug):
    article = Article.objects.get(slug = slug)
    return render(request,'articles/article_detail.html', {'article':article} )

@login_required()
def article_create(request):
    if request.method == 'POST':
        form = CreareArticle(request.POST, request.FILES)
        if form.is_valid():
            #saving to db
            instance = form.save(commit = False)
            instance.author = request.user
            instance.save()
            return redirect('articles:list')
        else:
            form = CreareArticle()
            return render(request,'articles/create.html',{'form':form})
    else:
        form = CreareArticle()
        return render(request,'articles/create.html',{'form':form})
