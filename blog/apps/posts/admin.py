from django.contrib import admin
from .models import Categoria, Post, Articulo
# Register your models here.



@admin.register(Post)
class PostsAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'subtitulo', 'fecha', 'texto', 'activo', 'categoria' , 'imagen', 'publicado')


# admin.site.register(Categoria)


@admin.register(Articulo)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'resumen', 'contenido', 'fecha_publicacion', 'imagen', 'estado', 'categoria', 'publicado')



admin.site.register(Categoria)  