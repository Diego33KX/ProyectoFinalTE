from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.producto_index, name = 'Index'),
    path('producto/<int:producto_id>/', views.index_view, name='producto'),
    path('registrarVenta/',views.registrar_venta, name='Registro')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
