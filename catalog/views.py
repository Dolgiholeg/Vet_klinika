from django.shortcuts import render
from .models import *
from django.contrib.auth.models import User
# Create your views here.
def index(req):
    numklient = Klient.objects.all().count()
    numporoda = Poroda.objects.all().count()
    numdisease = Disease.objects.all().count()
    if req.user.username:
        fname = req.user.first_name
        lname = req.user.last_name
    else:
        fname = 'ГОСТЬ'
        lname = 'ЗАРЕГИСТРИРУЙТЕСЬ'
    data = {'k1': numklient, 'k2': numporoda, 'k3': numdisease, 'fname':fname, 'lname':lname}
    return render(req, 'index.html', context=data)

#def allklient(req):
    #return render(req, 'index.html')

from django.views import generic
class Klientlist(generic.ListView):
    model = Klient

class KlientDetail(generic.DetailView):
    model = Klient

#from django.http import HttpResponse
#def info(req,id):
    #klient = Klient.objects.get(id=id)
    #return HttpResponse(klient.name)

from .form import SignUpform
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect

def registr(req):
    if req.POST:
        anketa = SignUpform(req.POST)
        if anketa.is_valid():
            anketa.save()
            k1 = anketa.cleaned_data.get('username')
            k2 = anketa.cleaned_data.get('password1')
            k3 = anketa.cleaned_data.get('first_name')
            k4 = anketa.cleaned_data.get('last_name')
            k5 = anketa.cleaned_data.get('email')
            user = authenticate(username=k1, password=k2)
            man = User.objects.get(username=k1)
            man.email = k5
            man.first_name = k3
            man.last_name = k4
            man.save()
            login(req, user)
            return redirect('home')

    else:
        anketa = SignUpform()
    data = {'regform': anketa}
    return render(req, 'registration/registration.html', context=data)
