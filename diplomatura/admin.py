from django.contrib import admin

class ProductoAdmin(admin.ModelAdmin):   #Filtro para el panel de administracion y mostrar lo que se decida en el orden que se elija
    fields = ['categoria', 'fecha_publicacion', 'nombre', 'imagen']

from diplomatura.models import Producto, Categoria

admin.site.register(Producto,ProductoAdmin)
#admin.site.register(Producto)
admin.site.register(Categoria)
