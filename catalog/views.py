from django.shortcuts import render
from .models import *
# Create your views here.
def index(req):
    numklient = Klient.objects.all().count()
    numporoda = Poroda.objects.all().count()
    numdisease = Disease.objects.all().count()
    data = {'k1': numklient, 'k2': numporoda, 'k3': numdisease}
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



