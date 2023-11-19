from django.http import HttpResponse, HttpResponseRedirect  # JsonResponse
from django.shortcuts import render, get_object_or_404

from .forms import ProductoForm
from .models import Producto


# Create your views here.
def index(request):
    # return HttpResponse("Hola Mundo!")
    productos = Producto.objects.all()  # .values()  # nos traera todos los elementos

    return render(request, "index.html", context={"productos": productos})
    # NOTE  RENDER: "render" es una función que se utiliza para mostrar una página web o una plantilla en tu sitio web. Puedes pensar en "render" como una especie de "constructor de páginas web". Esta función toma una plantilla HTML (que es como un esqueleto de tu página) y algunos datos (información que quieres mostrar en esa página), y luego combina todo eso para crear la página web final que se muestra en el navegador de un usuario.
    # NOTE return render(request, "index.html", context={"productos": productos}): Utiliza la función render para combinar una plantilla llamada "index.html" con un contexto que contiene los datos. En este caso, el contexto incluye un diccionario con la clave "productos" y el valor productos, que son los objetos Producto obtenidos de la base de datos. La función render toma esta plantilla y el contexto, genera una página HTML completa y la devuelve como respuesta al navegador del usuario.

    # productos = Producto.objects.filter(puntaje=3)  # aca le pasamos arhumentos nombrados
    # productos = Producto.objects.get(id=1) #trae un elemento en especifico
    # print(productos)
    # return HttpResponse("Hola Mundo!!!!") en la ruta http://127.0.0.1:8000/productos/ vemos que sale un Hola mundo!!!!
    # return HttpResponse(productos[0].nombre) retorna la pagina con el nombre del unico elemento q teniamos hecho hasta ese momento
    # return JsonResponse(list(productos), safe=False)

    # NOTE LO QUE HICIMOS FUE AGREMOS EL METODO DE VALUES PARA QUE NOS TRAJERA LOS VALORES DE CADA OBJETO DE PRODUCTO
    # TAMBIEN TUVIMOS QUE USAR LA CLASE DE JSONRESPONSE Y NUESTROS TUVIMOS Q TRANSFORMARLOS EN UNA LISTA Y A JSON RESPONSE EL SAFE LO CAMBIAMOS A FALSE


def detalle(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    return render(request, "detalle.html", context={"producto": producto})


def formulario(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/productos")
    else:
        form = ProductoForm()

    return render(request, "producto_form.html", {"form": form})
