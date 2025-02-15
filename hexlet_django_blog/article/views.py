from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.shortcuts import redirect
from django.urls import reverse


def index(request, tags, article_id):
    return render(request, 'articles/index.html', context={
        'tags': tags, 'article_id': article_id
    })


class IndexView(View):

    def get(self, request, *args, **kwargs):
        return redirect(reverse("article", kwargs={'tags': "python", 'article_id': 42}))

# Create your views here.
