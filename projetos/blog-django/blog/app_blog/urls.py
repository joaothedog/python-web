from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts, name='posts'),
    path('create/', views.add_post, name="add_post"),
    path('categoria/<int:categoria_id>', views.posts_por_categoria, name='posts_por_categoria')
]
