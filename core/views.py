from django.shortcuts import render, redirect
from core.models import evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.


def login_user(request):
    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return redirect('/')


def submit_login(request):
    if request.POST:
        username = request.POST.get('userName')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        print(usuario)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, "Usuario ou senha invalido")
    return redirect('/')


@login_required(login_url='/login/')
def lista_eventos(request):
    usuario = request.user
    event = evento.objects.filter(usuario=usuario)
    dados = {'eventos': event}
    return render(request, 'agenda.html', dados)


@login_required(login_url='/login/')
def evento_tela(request):
    id_evento = request.GET.get('id')
    dados = {}
    if id_evento:
        dados['evento'] = evento.objects.get(id=id_evento)
    return render(request, 'evento.html', dados )


@login_required(login_url='/login/')
def submit_evento(request):
    if request.POST:
        titulo = request.POST.get('titulo')
        data_evento = request.POST.get('data_evento')
        descricao = request.POST.get('descricao')
        usuario = request.user
        id_evento = request.POST.get('id_evento')
        if id_evento:
            event = evento.objects.get(id=id_evento)
            if event.usuario == usuario:
                event.titulo = titulo
                event.descricao = descricao
                event.data_evento = data_evento
                event.save()
        else:
            evento.objects.create(titulo=titulo,
                                  data_evento=data_evento,
                                  descricao=descricao,
                                  usuario=usuario)
    return redirect('/')


@login_required(login_url='/login/')
def delete_evento(request, id_evento):
    usuario = request.user
    event = evento.objects.get(id=id_evento)
    if usuario == event.usuario:
        event.delete()

    return redirect('/')
