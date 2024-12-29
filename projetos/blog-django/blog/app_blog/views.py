from django.shortcuts import render, redirect
from .models import Post

def posts(request):
    postagens = Post.objects.all().order_by('-data')
    return render(request, 'app_blog/posts.html', {'postagens': postagens})

def add_post(request):
    if request.method == 'POST':
        titulo = request.POST['titulo']
        conteudo = request.POST['conteudo']
        Post.objects.create(titulo=titulo, conteudo=conteudo)
        return redirect('posts')
    return render(request, 'app_blog/add_post.html')