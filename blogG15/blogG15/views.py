from django.shortcuts import render
from django.http import HttpResponseNotFound
from apps.posts.models import Post


def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts':posts})

def about(request):
    return render(request, 'about.html')

def about (request):
    return render(request, 'about.html')

def pagina_404(request, exception):
    return HttpResponseNotFound('<h1>Página no encontrada</h1>')