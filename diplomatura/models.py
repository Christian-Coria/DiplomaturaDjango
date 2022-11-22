from django.db import models
from django.utils.html import format_html # permite agregar html al panel de administracion

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

    Borrador = 'Borrado'
    Publicado = 'Publicado'
    Retirado = 'Retirado'
    APROBACION_PRODUCTO = (
        (Borrador , 'Borrador'),
        (Publicado, 'Publicado'),
        (Retirado, 'Retirado')
    )

    estado = models.CharField(max_length=10, choices=APROBACION_PRODUCTO, default='Borrador') #default es por defecto toma =...
    nombre = models.CharField(max_length=200)
    fecha_publicacion = models.DateTimeField('Fecha de Publicacion')
    imagen = models.ImageField(upload_to="nombre/%Y/%m/%d", blank=True, null=True) 
    categoria = models.ManyToManyField(Categoria) # Relacion de muchos a muchos 
    ''' blank=True, null=True    se indica que por defecto puede no tener nada el campo
        upload_to="producto/%Y/%m/%d"    indicamos donde se graba '''

    def tipo_de_producto(self):   #el metodo se agrega en el admin.py
        if self.estado == 'Retirado':
            return format_html('<spam style="background-color: #f00; padding:7px;">{}</spam>', self.estado ) # le damos color a estado en el html
        elif self.estado == 'Publicado':
            return format_html('<spam style="color: #f0f;">{}</spam>',  self.estado)
        elif self.estado == 'Borrado':
            return format_html('<spam style="color: #099;">{}</spam>',  self.estado)

    def __str__(self):
        return self.nombre + "----" +str(self.fecha_publicacion)
                                    #combertimos a string la fecha


