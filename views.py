from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect #agregado por mi
from .models import pregunta, eleccion
from django.template import loader #para usar index.html
from django.http import Http404
from django.urls import reverse
from django.views import generic
# Create your views here.


class IndexView(generic.ListView):
    template_name='aplicacion/index.html'
    context_object_name = 'listar_ultimas_preguntas'
    def get_queryset(self):
        return pregunta.objects.order_by('-pub_calendario')[:5]

class DetallesView(generic.DetailView):
    model=pregunta
    template_name="aplicacion/detalles.html"

class ResultadosView(generic.DetailView):
    model=pregunta
    template_name="aplicacion/resultados.html"


def votar(request, id_pregunta):
    preguntas = get_object_or_404(pregunta, pk=id_pregunta)
    print("id: ", id_pregunta)
    try:
         
        print("holi")
        
        opcion_seleccionada = preguntas.eleccion_set.get(pk=request.POST['elecciones'])
        
    except (KeyError, eleccion.DoesNotExist):
        print(KeyError, eleccion.DoesNotExist)
        print("holi2")
        return render(request, 'aplicacion/detalles.html',{'pregunta':preguntas,
        'error_message':"No seleccionaste nada bitch!", 
        })
    else:
        print("holi3")
        opcion_seleccionada.votos +=1
        opcion_seleccionada.save()
        return HttpResponseRedirect(reverse('appli:resultados', args=(preguntas.id,)))
        #return HttpResponse("Estas votando: %s" %id_pregunta) 