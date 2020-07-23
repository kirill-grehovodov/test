from django.shortcuts import render
from webapp.models import Article
from django.http import HttpResponseRedirect, HttpResponseNotFound, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse


def index_view(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'index.html', context)


def article_view(request, pk):
    # article_id = request.GET.get('pk')
    # try:
    #     article = Article.objects.get(pk=pk)
    # except Article.DoesNotExist:
    #     # return HttpResponseNotFound('not found')
    #     raise Http404

    article = get_object_or_404(Article, pk=pk)
    context = {'article': article}
    return render(request, 'article_view.html', context)


def article_create_view(request, *args, **kwargs):
    if request.method == 'GET':
        return render(request, 'article_create.html')
    elif request.method == 'POST':
        title = request.POST.get('title')
        text = request.POST.get('text')
        author = request.POST.get('author')
        article = Article.objects.create(title=title, text=text, author=author)

        # context = {'article': article}
        # return render(request, 'article_view.html', context)

        # return HttpResponseRedirect(f'/article?pk={article.pk}')

        # return HttpResponseRedirect(f'/article/{article.pk}/')

        # url = reverse('article_view', kwargs={'pk': article.pk})
        # return HttpResponseRedirect(url)

        return redirect('article_view', pk=article.pk)



