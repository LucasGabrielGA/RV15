from django.shortcuts import render
from django.http import HttpResponseNotFound
from apps.posts.models import Post, Categoria


def index(request):
    posts = Post.objects.all()
    categorias = Categoria.objects.all()
    return render(request, 'index.html', {'posts':posts, 'categorias':categorias})

def about(request):
    return render(request, 'about.html')

def about (request):
    return render(request, 'about.html')

def pagina_404(request, exception):
    return HttpResponseNotFound('<h1>Página no encontrada</h1>')