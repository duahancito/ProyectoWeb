from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Carrito, Producto, ItemCarrito


def index(request):
    productosAll = Producto.objects.all() # SELECT * FROM producto
    page = request.GET.get('page', 1) # OBTENEMOS LA VARIABLE DE LA URL, SI NO EXISTE NADA DEVUELVE 1
    try:
        paginator = Paginator(productosAll, 4)
        productosAll = paginator.page(page)
    except:
        raise Http404

    data = {
        'listado': productosAll,
        'paginator': paginator
    }
    return render(request, 'core/index.html', data)

def product(request):
    productosAll = Producto.objects.all() # SELECT * FROM producto
    page = request.GET.get('page', 1) # OBTENEMOS LA VARIABLE DE LA URL, SI NO EXISTE NADA DEVUELVE 1
    try:
        paginator = Paginator(productosAll, 8)
        productosAll = paginator.page(page)
    except:
        raise Http404

    data = {
        'listado': productosAll,
        'paginator': paginator
    }
    return render(request, 'core/product.html', data)

# CRUD
def add(request):
    data = {
        'form' : ProductoForm()
    }

    if request.method == 'POST':
        formulario = ProductoForm(request.POST, files=request.FILES) # OBTIENE LA DATA DEL FORMULARIO
        if formulario.is_valid():
            formulario.save() # INSERT INTO.....
            #data['msj'] = "Producto guardado correctamente"
            messages.success(request, "Producto almacenado correctamente")

    return render(request, 'core/add-product.html', data)

def update(request, id):
    producto = Producto.objects.get(id=id) # OBTIENE UN PRODUCTO POR EL ID
    data = {
        'form' : ProductoForm(instance=producto) # CARGAMOS EL PRODUCTO EN EL FORMULARIO
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES) # NUEVA INFORMACION
        if formulario.is_valid():
            formulario.save() # INSERT INTO.....
            #data['msj'] = "Producto actualizado correctamente"
            messages.success(request, "Producto actualizado correctamente")
            data['form'] = formulario # CARGA LA NUEVA INFOR EN EL FORMULARIO

    return render(request, 'core/update-product.html', data)

def delete(request, id):
    producto = Producto.objects.get(id=id) # OBTIENE UN PRODUCTO POR EL ID
    producto.delete()

    return redirect(to="index")

    
def about(request):
    return render(request, 'core/about.html',)


def blog(request):
    return render(request, 'core/blog.html')


def contact(request):
    return render(request, 'core/contact.html')


def detail(request):
    return render(request, 'core/detail.html')


def price(request):
    return render(request, 'core/price.html')


def service(request):
    return render(request, 'core/service.html')


def team(request):
    return render(request, 'core/team.html')


def testimonial(request):
    return render(request, 'core/testimonial.html')


#Carrito

def carrito(request):
    carrito = Carrito.objects.get(usuario=request.user)
    items = ItemCarrito.objects.filter(carrito=carrito)
    total = sum(item.subtotal() for item in items)
    return render(request, 'core/carrito.html', {'carrito': carrito, 'items': items, 'total': total})

def agregar_producto(request, producto_id):
    producto = Producto.objects.get(pk=producto_id)
    carrito = Carrito.objects.get(usuario=request.user)

    item, created = ItemCarrito.objects.get_or_create(carrito=carrito, producto=producto)
    item.cantidad += 1
    item.save()

    return redirect('carrito')

def eliminar_producto(request, item_id):
    item = ItemCarrito.objects.get(pk=item_id)
    item.delete()
    return redirect('carrito')

#Rastreo
def rastreo(request):
    carrito = Carrito.objects.get(usuario=request.user)
    items = ItemCarrito.objects.filter(carrito=carrito)
    total = sum(item.subtotal() for item in items)
    return render(request, 'core/rastreo.html', {'carrito': carrito, 'items': items, 'total': total})

#PagoCarro
def pagocarro(request):
    carrito = Carrito.objects.get(usuario=request.user)
    items = ItemCarrito.objects.filter(carrito=carrito)
    total = sum(item.subtotal() for item in items)
    return render(request, 'core/pagocarro.html', {'carrito': carrito, 'items': items, 'total': total})

