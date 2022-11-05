from django.urls import path
#from diplomatura.views import index      
from diplomatura import views
urlpatterns = [
    #path('', index, name="index"),
    path('', views.index, name='index')
    
    
]
