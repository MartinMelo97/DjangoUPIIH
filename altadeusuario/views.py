from django.shortcuts import render, redirect
from django import views
from .models import AltaUsuario


class AltaUsuarioList(views.View):
    def get(self, request):
        altausuario1 = AltaUsuario.objects.all()
        context = {
            'altausuario2' : altausuario1
        }
        template_name = 'altadeusuario/list.html'
        return render(request, template_name, context)

class AltaUsuarioDetail(views.View):
    def get(self, request, id):
        altausuario5 = AltaUsuario.objects.get(id=id)
        context = {
            'altausuario6' : altausuario5
        }
        template_name = 'altadeusuario/detail.html'
        return render(request, template_name, context)

class AgregarAltaUsuario(views.View):
    def get(self, request):
        print('llego')
        template_name = 'altadeusuario/form.html'
        context = {
            'action': 'create'
        }
        return render(request, template_name, context)

    def post(self, request):
        identificacion = request.POST['identificacion']
        Nombre = request.POST['Nombre']
        Apellidos = request.POST['Apellidos']
        Puesto = request.POST['Puesto']
        Horario = request.POST['Horario']
        Descanso = request.POST['Descanso']
        Perfiles = request.POST['Perfiles']
        altausuario7 = AltaUsuario.objects.create(
            identificacion=identificacion,
            Nombre = Nombre,
            Apellidos= Apellidos,
            Puesto=Puesto,
            Horario=Horario,
            Descanso=Descanso,
            Perfiles=Perfiles
        )
        context = {
            'action': 'create'
        }
        return redirect('/altadeusuario')

class ModificarAltaUsuario(views.View):
    def get(self, request, id):
        altausuario10 = AltaUsuario.objects.get(id=id)
        context = {
            'altausuario11' : altausuario10,
            'action' : 'edit'
        }
        template_name = 'altadeusuario/form.html'
        return render(request, template_name, context)

    def post(self, request, id):
        altausuario13 = AltaUsuario.objects.get(id=id)
        altausuario13.identificacion = request.POST['identificacion']
        altausuario13.Nombre = request.POST['Nombre']
        altausuario13.Apellido = request.POST['Apellidos']
        altausuario13.Puesto = request.POST['Puesto']
        altausuario13.Horario = request.POST['Horario']
        altausuario13.Descanso = request.POST['Descanso']
        altausuario13.Perfiles = request.POST['Perfiles']
        altausuario13.save()
        return redirect('/altadeusuario/', altausuario13.id)

class EliminarAltaUsuario(views.View):
    def get(self, request, id):
        altausuario15 = AltaUsuario.objects.get(id=id)
        altausuario15.delete()
        return redirect('/altadeusuario/')


