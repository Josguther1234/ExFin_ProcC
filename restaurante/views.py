from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .forms import CartaForm
from .models import Menu, Plato, Carta
from django.contrib import messages

def menu_list(request):
    menus = Carta.objects.all()
    return render(request, 'menu_list.html', {'menus': menus})

def menu_plato(request):
    menus = Plato.objects.all()
    return render(request, 'menu_plato.html', {'menus': menus})

def menu_solo(request):
    menus = Menu.objects.all()
    return render(request, 'menu_solo.html', {'menus': menus})
def crearcarta(request):
    menus = Carta.objects.all()
    return render(request, 'crearcarta.html', {'menus': menus})

def crearcarta2(request):
    if request.method == "POST":
        formulario = CartaForm(request.POST)
        if formulario.is_valid():
            menu = menu.objects.create(nombre=formulario.cleaned_data['menu'])
            for plato_id in request.POST.getlist('plato'):
                carta = Carta(plato_id=plato_id, menu_id = menu_id)
                carta.save()
            return redirect('menu_list')
    else:
        formulario = CartaForm()
    return render(request, 'crearcarta.html', {'formulario': formulario})
