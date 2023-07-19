from django.db import models
from django.utils import timezone
# Create your models here.



#Categoria:
class Categoria(models.Model):
    nombre = models.CharField(max_length=30, null=False)

    def __str__(self):
        return self.nombre
    


# Post
class Post(models.Model):
    titulo = models.CharField(max_length=50, null=False)
    subtitulo = models.CharField(max_length=100, null=True, blank=True)
    fecha = models.DateTimeField(auto_now_add=True)
    texto = models.TextField(null=False)
    activo = models.BooleanField(default=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, default='Sin categoria')
    imagen = models.ImageField(null=True, blank=True, upload_to='post', default='static/post_default.png')
    publicado = models.DateTimeField(default=timezone.now)
    class Meta:
        ordering = ('-publicado',)

    def __str__(self):
        return self.titulo
    
    def delete(self, using = None, keep_parent = False):
            self.imagen.delete(self.imagen.name)
            super().delete()




    
# Articulo


class Articulo(models.Model):
    # def __init__(self, id_usuario, id_articulo, titulo, resumen, contenido, imagen):
    
    titulo = models.CharField(max_length=30, null=False)
    resumen = models.TextField(null=False)
    contenido = models.TextField(null=False)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(null=True, blank=True, upload_to='articulo', default='articulo/default_articulo.jpg')
    estado = models.BooleanField(default=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, default='Sin categoria')
    publicado = models.DateTimeField(default=timezone.now)
    class Meta:
        ordering = ('-publicado',)

    def __str__(self):
        return self.titulo
    
    def delete(self, using = None, keep_parent = False):
            self.imagen.delete(self.imagen.name)
            super().delete()







# class Comentario:

#     def __init__(self, id_articulo, id_usuario, contenido):
#         self.id = Comentario.id_counter
#         Comentario.id_counter += 1
#         self.id_articulo = id_articulo
#         self.id_usuario = id_usuario
#         self.contenido = contenido
#         self.fecha_hora = datetime.now()
#         self.estado = 'activo'

# -------------------------------------------
# class Comentario:

#     def __init__(self, id_articulo, id_usuario, contenido):
#         self.id = Comentario.id_counter
#         Comentario.id_counter += 1

#         self.id_articulo = id_articulo
#         self.id_usuario = id_usuario
#         contenido = models.TextField(null=False)
#         fecha = models.DateTimeField(auto_now_add=True)
#         estado = models.BooleanField(default=True)



# from django.contrib.auth.models import User

# class Comentario(models.Model):
#     id_articulo = models.ForeignKey('Articulo', on_delete=models.CASCADE)
#     id_usuario = models.ForeignKey(User, on_delete=models.CASCADE)
#     contenido = models.TextField(null=False)
#     fecha = models.DateTimeField(auto_now_add=True)
#     estado = models.BooleanField(default=True)

#     def __str__(self):
#         return f"Comentario {self.id} - Artículo {self.id_articulo_id} - Usuario {self.id_usuario_id}"
