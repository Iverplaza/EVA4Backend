from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from CRUD.models import Clase, Estudiante, Profesor


# Create your views here.
def crear_clase(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        horario = request.POST.get('horario')
        descripcion = request.POST.get('descripcion')

        Clase.objects.create(nombre=nombre,horario=horario,descripcion=descripcion)
        return redirect('ver_clase')
    return render(request,'crear_clase.html')

def ver_clase(request):
    clase = Clase.objects.all()
    print(clase)
    contexto = {'clase':clase}
    return render(request,'ver_clase.html',contexto)

def actualizar_clase(request,id):
    
    clase=get_object_or_404(Clase,id=id)
    print(clase.nombre)
    print(clase.horario)
    print(clase.descripcion)
    if request.method == 'POST':
        clase.nombre = request.POST.get('clase')
        clase.horario = request.POST.get('horario')
        clase.descripcion = request.POST.get('descripcion')
        
        clase.save()
        
        return redirect('ver_clase')
    return render(request,'actualizar_clase.html',{'clase':clase})

def eliminar_clase(request, id):
   
    clase=get_object_or_404(Clase,id=id)
    if request.method == 'POST':
        clase.delete()
      
        return redirect('ver_clase')
    return render(request,'eliminar_clase.html',{'clase':clase})
#----------------------------------------------------------------------------------------------------
def crear_estudiante(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        correo = request.POST.get('correo')
        clases_inscritas = request.POST.get('clases_inscritas')

        Estudiante.objects.create(nombre=nombre,corrreo=correo,clases_inscritas=clases_inscritas)
        return redirect('ver_estudiante')
    return render(request,'crear_estudiante.html')

def ver_estudiante(request):
    estudiante = Estudiante.objects.all()
    print(estudiante)
    contexto = {'estudiante':estudiante}
    return render(request,'ver_estudiante.html',contexto)

def actualizar_estudiante(request,id):
    
    estudiante=get_object_or_404(Estudiante,id=id)
    print(estudiante.nombre)
    print(estudiante.correo)
    print(estudiante.clases_inscritas)
    if request.method == 'POST':
        estudiante.nombre = request.POST.get('nombre')
        estudiante.correo = request.POST.get('correo')
        estudiante.clases_inscritas = request.POST.get('clases_inscritas')
        
        estudiante.save()
        
        return redirect('ver_estudiante')
    return render(request,'actualizar_estudiante.html',{'estudiante':estudiante})

def eliminar_estudiante(request, id):
   
    estudiante=get_object_or_404(Estudiante,id=id)
    if request.method == 'POST':
        estudiante.delete()
      
        return redirect('ver_estudiante')
    return render(request,'eliminar_estudiante.html',{'estudiante':estudiante})
#--------------------------------------------------------------------------------------
def crear_profesor(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        especialidad = request.POST.get('especialidad')
        clases_impartidas = request.POST.get('clases_impartidas')

        Profesor.objects.create(nombre=nombre,especialidad=especialidad,clases_impartidas=clases_impartidas)
        return redirect('ver_profsor')
    return render(request,'crear_profesor.html')

def ver_profesor(request):
    profesor = Profesor.objects.all()
    print(profesor)
    contexto = {'profesor':profesor}
    return render(request,'ver_profesor.html',contexto)

def actualizar_profesor(request,id):
    
    profesor=get_object_or_404(Profesor,id=id)
    print(profesor.nombre)
    print(profesor.especialidad)
    print(profesor.clases_impartidas)
    if request.method == 'POST':
        profesor.nombre = request.POST.get('nombre')
        profesor.especialidad = request.POST.get('especialidad')
        profesor.clases_impartidas = request.POST.get('clases_impartidas')
        
        profesor.save()
        
        return redirect('ver_profesor')
    return render(request,'actualizar_profesor.html',{'profesor':profesor})

def eliminar_profesor(request, id):
   
    profesor=get_object_or_404(Profesor,id=id)
    if request.method == 'POST':
        profesor.delete()
      
        return redirect('ver_profesor')
    return render(request,'eliminar_profesor.html',{'profesor':profesor})
