from django.shortcuts import render
from .models import Post, Articulo
from django.views import View


# Create your views here.


def posts(request):
    posts = Post.objects.all()
    return render(request, 'post.html', {'posts' : posts})

# Vista basada en funcion
def articulos(request):
    articulos = Articulo.objects.all()
    return render(request, 'articulo.html', {'articulos' : articulos})

# vista basada en clases
# class ArticuloView(View):
#     template_name= 'articulo.html'

#     def get(self, request):
#         articulos = Articulo.objects.all()
#         return render(request, 'articulo.html', {'articulos' : articulos})

