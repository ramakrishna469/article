from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from forms import ArticleForm
from models import Article


def article_list(request):
	articles = Article.objects.all()
	return render(request, 'article/article_list.html',{'articles':articles})

def add_article(request):
	form = ArticleForm()
	if request.method=="POST":
		form = ArticleForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/article/')
	return render(request,'article/add_article.html',{'form':form})