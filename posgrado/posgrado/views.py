from django.shortcuts import render
#from django.http import HttpResponse
#from django.template import loader

# Create your views here.
def home(request):
    #pagina = "<html><body><h1>Posgrado en Electrónica</h1></body></html>"
    #return HttpResponse(pagina)
    #template = loader.get_template("templates/index.html")
    #template = loader.get_template("posgrado/index.html")
    context = {}

    #return HttpResponse(template.render(context, request))
    return render(request, 'posgrado/index.html', context)