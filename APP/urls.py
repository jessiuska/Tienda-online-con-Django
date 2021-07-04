from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = "APP"
urlpatterns = [
    path('', views.index, name="index"),
    path('acercade/', views.acercade, name="acercade"),
    path('contacto/', views.contacto, name="contacto"),
    path('busqueda/', views.busqueda, name="busqueda"),
    path('productos/<int:pk>', views.productosDetalles, name="productos"),
    path('alta', views.alta, name="alta"),
    path('modificar/<int:pk>', views.modificar, name="modificar"),
    path('eliminar/<int:pk>', views.eliminar, name="eliminar"),
    
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)