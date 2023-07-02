from django.shortcuts import render,redirect
from django.http import HttpResponse
from gestionReservas.models import *
from gestionReservas.forms import *



def login(request):

    form = loginForm()

    return render(request, "Login.html", {"form":form})

def log(request):

    request.session["user"] = request.POST["usuario"]
    existe = Users.objects.filter(name=request.POST["usuario"], password=request.POST["clave"]).exists()

    if existe:

        user = Users.objects.get(name=request.POST["usuario"], password=request.POST["clave"])
        if user.isAdmin:
            return redirect("/userAdmin/")
            
        else:
            return redirect("/user/")
    
    else:

        return redirect("/login/")

def us(request):
    
    try:
        return render(request, "usuarionormal.html",{"user": request.session["user"]})
    except:
        return redirect("/login/")
    
def usAdmin(request):
    
    try:
        return render(request, "user.html",{"user": request.session["user"]})
    except:
        return redirect("/login/")

def mostrarUsuarios(request):

    users = Users.objects.all()

    form = addUser()

    return render(request, "GestionUsuarios.html", {"users":users, "form":form})

def mostrarReservas(request):

    form = addReserve()

    reserves = Reserves.objects.all()

    return render(request, "GestionReservas.html", {"form":form, "reserves":reserves})
    

def agregarUsu(request):

    name = request.POST["name"]
    lastname = request.POST["lastname"]
    pswd = request.POST["password"]
    try:
        if request.POST["isAdmin"]:
            admin = True
    except:
        admin = False
    newUser = Users(name=name,lastname=lastname,password=pswd,isAdmin=admin)
    newUser.save()

    return redirect("/verUsuarios/")

def eliminarUsu(request, id):

    user = Users.objects.get(id=id)
    user.delete()
    return redirect("/verUsuarios/")

def agregarRes(request):

    usuario = request.POST["usuario"]
    date = request.POST["date"]
    time = request.POST["time"]
    hora = Hours(date=date,time=time)
    hora.save()
    
    reserva = Reserves(idUser=Users.objects.get(id=usuario) , idHour=hora)
    reserva.save()
    return redirect("/verReservas/")

def eliminarRes(request, id):
    
    res = Reserves.objects.get(id=id)
    res.delete()

    return redirect("/verReservas/")