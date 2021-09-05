from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm
from django.views.generic import DetailView, UpdateView, DeleteView

# Create your views here.


class NewsDetailView(DetailView):
    model = Article
    template_name = 'news/detail_view.html'
    context_object_name = 'article'


class NewsUpdateView(UpdateView):
    model = Article
    template_name = 'news/create.html'
    form_class = ArticleForm


class NewsDeleteView(DeleteView):
    model = Article
    success_url = '/news'
    template_name = 'news/news-delete.html'


def news_home(request):
    news = Article.objects.all()
    data = {
        'title': 'Новости',
        'news': news
    }
    return render(request, 'news/news_home.html', data)


def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = 'Форма неверно заполнена'
    af = ArticleForm()
    data = {
        'title': 'Добавить запись',
        'form': af,
        'error': error
    }
    return render(request, 'news/create.html', data)


