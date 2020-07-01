from django.shortcuts import render, redirect
from core.models import evento
# Create your views here.


def lista_eventos(request):
    #usuario = request.user
    #event = evento.objects.filter(usuario=usuario)
    event = evento.objects.all()
    dados = {'eventos': event}
    return render(request, 'agenda.html', dados)


#def index(request):
#    return redirect('/agenda/')
