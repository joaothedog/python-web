from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Categoria

def posts(request):
    categorias = Categoria.objects.all()
    categoria_id = request.GET.get('categoria') 

    if categoria_id:
        postagens = Post.objects.filter(categoria_id=categoria_id).order_by('-data')
    else:
        postagens = Post.objects.all().order_by('-data')

    return render(request, 'app_blog/posts.html', {'postagens': postagens, 'categorias': categorias})

def add_post(request):
    if request.method == 'POST':
        titulo = request.POST['titulo']
        conteudo = request.POST['conteudo']
        categoria_id = request.POST['categoria']
        categoria = Categoria.objects.get(id=categoria_id)
        Post.objects.create(titulo=titulo, conteudo=conteudo, categoria=categoria)
        return redirect('posts')
    
    categorias = Categoria.objects.all()
    return render(request, 'app_blog/add_post.html', {'categorias': categorias})

def posts_por_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    postagens = categoria.posts.all()
    categorias = Categoria.objects.all()
    return render(request, 'app_blog/posts_por_categoria.html', {'postagens': postagens, 'categoria': categoria,'categorias': categorias})
