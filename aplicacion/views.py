from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
from .models import Categoria, Producto

def index(request):
  
  categorias= Categoria.objects.order_by('nombre')
  if request.method == 'POST':
    id_categoria= request.POST.get('categoria_id')
    if id_categoria != 'null':
      product_list= Producto.objects.filter(categoria_id=id_categoria)    
    else:
      product_list= Producto.objects.order_by('nombre')
  else:
    product_list= Producto.objects.order_by('nombre')
  
  context= {'product_list': product_list, 'categorias': categorias}
  return render(request, 'product/index.html', context)

def create(request):
  categorias= Categoria.objects.order_by('nombre')
  context = {'categorias': categorias}
  return render(request, 'product/create.html', context)

def store(request):
  if request.method == 'POST':
    categoria_id= int(request.POST.get('id_categoria'))
    nombre= request.POST.get('nombre')
    precio= request.POST.get('precio')
    stock= request.POST.get('stock')
    upload= request.POST.get('upload')
    pub_date= '2023-10-13'
    
    Producto.objects.create(
      categoria_id= categoria_id,
      nombre= nombre,
      precio= precio,
      stock= stock,
      upload= upload,
      pub_date= pub_date
    )
    return redirect('index')
  return HttpResponse('ERROR')

def show(request, id= None):
  producto= Producto.objects.get(id= id)
  
  if producto.stock < 10:
    color= 'text-danger'
  else:
    color= 'text-primary'

  context= {
    'producto': producto,
    'colorstock': color
    }
  return render(request, 'product/show.html', context)
    
def edit(request, id= None):
  categorias= Categoria.objects.order_by('nombre')
  producto= Producto.objects.get(id= id)
  context= {'producto': producto, 'categorias': categorias}
  return render(request, 'product/edit.html', context)


def update(request, id= None):
  if request.method == 'POST':
    categoria_id= int(request.POST.get('id_categoria'))
    nombre= request.POST.get('nombre')
    precio= request.POST.get('precio')
    stock= request.POST.get('stock')
    upload= request.POST.get('upload')
    pub_date= '2023-10-13'
    
    producto= Producto.objects.get(id= id)
    producto.categoria_id= categoria_id
    producto.nombre= nombre
    producto.precio= precio
    producto.stock= stock
    producto.upload= upload
    producto.pub_date= pub_date
    producto.save()
    
    return redirect('index')
  return HttpResponse('ERROR')