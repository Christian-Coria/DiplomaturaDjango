from django.contrib import admin
from diplomatura.models import Producto, Categoria


class ProductoAdmin(admin.ModelAdmin):   #Filtro para el panel de administracion y mostrar lo que se decida en el orden que se elija
    #fields = ['categoria', 'fecha_publicacion', 'nombre', 'imagen']
    fieldsets = [
        ("Relacion", {"fields": ["categoria"]}),
        ("Datos generales", 
             {"fields": 
                 ['fecha_publicacion', 'nombre', 'estado' ,'imagen']}

        )
    ]


admin.site.register(Producto,ProductoAdmin)
#admin.site.register(Producto)
admin.site.register(Categoria)
