from django.shortcuts import render, HttpResponse, redirect
from .models import Dojo, Ninja

# Create your views here.
def index(request):
    context = {
        "all_dojos": Dojo.objects.all()
    }
    return render(request, "index.html", context)



def dojos(request):
    if request.method == 'POST':
        some_dojo = Dojo.objects.create(name=request.POST['name'], city=request.POST['city'], state=request.POST['state'])
    return redirect('/')


def ninjas(request):
    if request.method == 'POST':
        one_ninja = Ninja.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], dojo_id=int(request.POST['all_dojos']))
    return redirect('/')


def destroy(request, dojos_id):
    try:
        a_dojo = Dojo.objects.get(id=dojos_id)
        a_dojo.delete()
    except:
        print('its not working')
    return redirect('/')