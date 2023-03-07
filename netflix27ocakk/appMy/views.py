from django.shortcuts import render
from appUser.models import *
from .models import *
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    context = {"title":"Anasayfa"}
    return render(request,'index.html',context)

@login_required(login_url='loginUser')
def indexBrowse(request,pid):
    context = {"title":"Netflix"}
    profil = Profil.objects.get(id=pid)
    category = Category.objects.all()
    en_populer = Dizilerim.objects.all().order_by('-date_now')[:6]
    en_cok_goruntulenen = Dizilerim.objects.all().order_by('?')[:6]
    context.update({
        "profil": profil,
        'category':category,
        'en_populer':en_populer,
        'en_cok_goruntulenen':en_cok_goruntulenen,
    })
    return render(request,'browse-index.html',context)

def browseIcerik(request,pid,did,id):
    profil = Profil.objects.get(id=pid)
    diziler = Dizilerim.objects.filter(category = id)
    category = Category.objects.all()
    categor = Category.objects.get(id = id)
    
    context = {"title":categor}
    context.update({
        "profil": profil,
        'category':category,
        'diziler':diziler,
    })   
    return render(request, 'browse-icerik.html',context)

