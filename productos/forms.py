from . import models
from django.forms import ModelForm


class ProductoForm(ModelForm):
    class Meta:  # La clase Meta se utiliza para proporcionar configuración adicional para el formulario, como qué modelo debe usarse y qué campos del modelo deben incluirse en el formulario.
        model = models.Producto
        fields = ["nombre", "stock", "puntaje", "categoria"]


# En resumen, este código de Django define un formulario llamado ProductoForm que se basa en el modelo Producto. El formulario incluye campos para recopilar información sobre productos, como el nombre, el stock, el puntaje y la categoría, y se utiliza para ingresar datos en la base de datos de acuerdo con la estructura del modelo Producto.
