# from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.shortcuts import redirect
from django.urls import reverse
from hexlet_django_blog.article.models import Article
from hexlet_django_blog.article.forms import ArticleForm
from django.contrib import messages


class ArticleCreateView(View):
    template_name = 'articles/create.html'

    def get(self, request, *args, **kwargs):
        form = ArticleForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Данные успешно сохранены!')
            return redirect(reverse('articles_index'))
        else:
            messages.error(request, 'Ошибка ввода данных!')
            return render(request, self.template_name, {'form': form})


class IndexView(View):

    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(request, 'articles/index.html', context={
            'articles': articles,
        })


class ArticleView(View):

    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['id'])
        return render(request, 'articles/show.html', context={
            'article': article,
        })
# Create your views here.

class ArticleFormEditView(View):

    def get(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        form = ArticleForm(instance=article)
        return render(request, 'articles/update.html', {'form': form, 'article_id':article_id})

    def post(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            messages.success(request, 'Данные успешно сохранены!')
            return redirect('articles_index')

        messages.error(request, 'Ошибка ввода данных!')
        return render(request, 'articles/update.html', {'form': form, 'article_id': article_id})

class ArticleFormDeleteView(View):

    def post(self, request, *args, **kwargs):
        article_id = kwargs.get('id')
        article = Article.objects.get(id=article_id)
        if article:
            article.delete()
            messages.success(request, 'Данные успешно удалены!')
        return redirect('articles_index')
