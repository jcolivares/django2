from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.
from .models import Articulo, TipoArticulo

def index(request):
    pubs = Articulo.objects.all()
    context = {
        "pubs": pubs
    }
    return render(request, "publicaciones/index.html", context)

"""
def car_detail(request, pk):
    
    car_objs = Car.objects.filter(owner_id=owner_obj.id)
    context = {
        "vehicles": car_objs,
        "drivers": owner_obj,
        }
    return render(request, "car_detail.html", context)
"""

