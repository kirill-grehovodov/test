from django.shortcuts import render
from django.views.generic import View, TemplateView, RedirectView
from webapp.forms import ArticleForm
from webapp.models import Article
from django.http import HttpResponseRedirect, HttpResponseNotFound, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse


class IndexView(View):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()
        context = {
            'articles': articles
        }
        return render(request, 'index.html', context)


class IndexRedirectView(RedirectView):
    pattern_name = 'index'

#
# def index_view(request):
#     articles = Article.objects.all()
#     context = {
#         'articles': articles
#     }
#     return render(request, 'index.html', context)

class ArticleView(TemplateView):
    template_name = 'article_view.html'
    #1
    def get_context_data(self, **kwargs):
        kwargs['article'] = get_object_or_404(Article, pk=kwargs['pk'])
        return super().get_context_data(**kwargs)
    #2
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['article'] = get_object_or_404(Article, pk=kwargs['article_pk'])
    #     return context


# def article_view(request, pk):
    #1
    # article_id = request.GET.get('pk')
    # try:
    #     article = Article.objects.get(pk=pk)
    # except Article.DoesNotExist:
    #     # return HttpResponseNotFound('not found')
    #     raise Http404
    #2
    # article = get_object_or_404(Article, pk=pk)
    # context = {'article': article}
    # return render(request, 'article_view.html', context)


def article_create_view(request, *args, **kwargs):
    if request.method == 'GET':
        form = ArticleForm()
        return render(request, 'article_create.html', context={'form': form})
    elif request.method == 'POST':
        form = ArticleForm(data=request.POST)
        if form.is_valid():
            article = Article.objects.create(
                title=form.cleaned_data['title'],
                author=form.cleaned_data['author'],
                text=form.cleaned_data['text']
            )
            return redirect('article_view', pk=article.pk)
        else:
            return render(request, 'article_create.html', context={'form': form})


        # context = {'article': article}
        # return render(request, 'article_view.html', context)

        # return HttpResponseRedirect(f'/article?pk={article.pk}')

        # return HttpResponseRedirect(f'/article/{article.pk}/')

        # url = reverse('article_view', kwargs={'pk': article.pk})
        # return HttpResponseRedirect(url)

def article_update_view(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'GET':
        form = ArticleForm(data={
            'title': article.title,
            'text': article.text,
            'author': article.author
        })
        return render(request, 'update.html', context={'form': form, 'article': article})
    elif request.method == 'POST':
        form = ArticleForm(data=request.POST)
        if form.is_valid():
            article.title = form.cleaned_data['title']
            article.text = form.cleaned_data['text']
            article.author = form.cleaned_data['author']
            article.save()
            return redirect('article_view', pk=article.pk)
        else:
            return render(request, 'update.html', context={'form': form, 'article': article})


def article_delete_view(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'GET':
        return render(request, 'delete.html', context={'article': article})
    elif request.method == 'POST':
        article.delete()
        return redirect('index')