from django.urls import path
from . import (
    views,
)  # aca le pedimos con el . que desde la carpeta q nos encontramos me importe el archivod e views.

app_name = "productos"
urlpatterns = [
    path("", views.index, name="index"),
    path("formulario", views.formulario, name="formulario"),
    path("<int:producto_id>", views.detalle, name="detalle"),
]
