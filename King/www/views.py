from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView

def www(request):
    news = Articles.objects.order_by('-date')
    return render(request, 'www/www.html', {'news': news})

class NewsDetailView(DetailView):
    model = Articles
    template_name = 'www/details.html'
    context_object_name = 'article'

class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'www/create.html'

    form_class = ArticlesForm

class NewsDeletelView(DeleteView):
    model = Articles
    success_url = '/www/'
    template_name = 'www/delete.html'

def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Ошибка'

    form = ArticlesForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'www/create.html', data)
