from django.contrib import admin
from diplomatura.models import Producto, Categoria

class ProductoInLine(admin.TabularInLine):
    model = Producto
    extra = 0 #indicamos la cantidad de productos que podemos agregar


class CategoriaAdmin(admin-ModelAdmin): #esta clase customiza ... asocia las clases
    inlines = [ProductoInLine]

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):   #Filtro para el panel de administracion y mostrar lo que se decida en el orden que se elija
    #fields = ['categoria', 'fecha_publicacion', 'nombre', 'imagen']
    fieldsets = [
        ("Relacion", {"fields": ["categoria"]}),
        ("Datos generales", 
             {"fields": 
                 ['fecha_publicacion', 'nombre', 'estado' ,'imagen']}

        )
    ]
    list_display = ['tipo_de_producto','nombre','fecha_publicacion', 'imagen'] #visualizamos en forma de columnas 
    ordering = ['-fecha_publicacion']    #ordenamos por fecha de publicacion en este caso el signo menos es para alterar el orden natural
    list_filter = ('nombre', 'fecha_publicacion',) # list_filter es una tupla que permite filtrar
    search_fields = ('nombre', 'estado',) # search_fields agrega opciones de busquedas
    list_display_links = ('nombre', 'fecha_publicacion',) #agrega links a cada columna para ingreso por click
    
    @admin.display(descripcion='Name')  #customizamos el panel con una logica ... en este caso cambia a mayuscula los objetos
    def upper_case_name(self, obj):
        return ("%s %s" % (obj.nombre, obj.estado)).upper() # pasamos a mayuscula el nombre y el estado


#admin.site.register(Producto,ProductoAdmin) en lugar de esta linea podemos replazar por el decorador @admin.register(Producto)
admin.site.register(Categoria,CategoriaAdmin)
#admin.site.register(Producto)
#admin.site.register(Categoria)
