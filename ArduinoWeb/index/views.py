from multiprocessing import context
from django.shortcuts import render, redirect
from index.controller import blueOn, greenOn, redOn , yellowOn, allOff
from .models import Products,Categories,Countries,Ventas
from django.shortcuts import get_object_or_404,render
# Create your views here.
def index_view (request,producto_id):
    producto = get_object_or_404(Products, pk=producto_id)
    context = {"producto": producto}
    if request.POST:
        id = request.POST['id']
        if int(id) == 1:
            redOn()
        elif int(id) == 2:
            greenOn()
        elif int(id) == 3:
            blueOn()
        elif int(id) == 4:
            yellowOn()
        elif int(id) == 5:
            allOff()
        print(id)
    return render(request, 'index.html',context)

def producto_index(request):
    product_list = Products.objects.all()
    context = {'product_list':product_list}
    return render(request, 'productos.html',context)

def registrar_venta(request):
    producto = request.POST['producto']
    precio = float(request.POST['precio'])
    cantidad = float(request.POST['cantidad'])
    subtotal = float(precio*cantidad)
    #fecha = request.POST['fecha']
    igv = float(subtotal*0.18)
    total = float(subtotal+igv)
    cliente = request.POST['cliente']
    venta = Ventas.objects.create(
        producto = producto,
        precio = precio,
        cantidad = cantidad,
        subtotal = subtotal,
        #fecha = fecha,
        igv = igv,
        total = total,
        cliente = cliente
    )
    
    if request.POST:
        id = request.POST['id']
        if int(id) == 1:
            redOn()
        elif int(id) == 2:
            greenOn()
        elif int(id) == 3:
            blueOn()
        elif int(id) == 4:
            yellowOn()
        elif int(id) == 5:
            allOff()
        print(id)
    return redirect('/')
