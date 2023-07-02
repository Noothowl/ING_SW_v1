import pytest
from gestionReservas.models import *
import datetime

@pytest.mark.django_db
def test_createUser():

    usuario = Users(name="Joaquin", lastname="Aguilar", password="1234", isAdmin=False)

    usuario.save()
    
    assert Users.objects.get(name = "Joaquin").name == "Joaquin"


@pytest.mark.django_db
def test_deleteUser():

    
    usuario = Users(name="Joaquin", lastname="Aguilar", password="1234", isAdmin=False)

    usuario.save()

    Users.objects.get(name="Joaquin").delete()
    

    assert not Users.objects.filter(name="Joaquin").exists()

@pytest.mark.django_db
def test_createReserve():

    usuario = Users(name="Joaquin", lastname="Aguilar", password="1234", isAdmin=False)

    usuario.save()

    fecha = datetime.date.today()
    hora = datetime.datetime.now().time()
    hour = Hours(date= fecha, time=hora)
    hour.save()

    Reserves(idUser=Users.objects.get(id=1), idHour=Hours.objects.get(id=1)).save()
    assert Reserves.objects.count() > 0

