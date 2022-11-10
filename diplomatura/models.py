from django.db import models

class Categoria(models.Model):
    clase = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)

    def __str__(self):
        return '%s'% self.clase

''' slug es un nombre de categoria o producto que va en la url 
        para busquedas del buscador google
db_index=True
    return '%s'% self.clase
'''



class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    fecha_publicacion = models.DateTimeField('Fecha de Publicacion')
    imagen = models.ImageField(upload_to="nombre/%Y/%m/%d", blank=True, null=True) 
    categoria = models.ManyToManyField(Categoria) # Relacion de muchos a muchos 
    ''' blank=True, null=True    se indica que por defecto puede no tener nada el campo
        upload_to="producto/%Y/%m/%d"    indicamos donde se graba '''

    def __str__(self):
        return self.nombre + "----" +str(self.fecha_publicacion)
                                    #combertimos a string la fecha


