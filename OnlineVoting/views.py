from django.http import HttpResponse
from django.shortcuts import render, redirect
from .form import *
from .models import Destination


# Create your views here.
def party_image_view(request):
    if request.method == 'POST':
        form = PartyForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = PartyForm()
    return render(request, 'party.html', {'form': form})


def party_del(request):
    u = Destination.objects.get(pk=id)
    if u:
        return redirect('party_del')
    return render(request, 'party_info.html', {'dest1': dest1})


def party_info(request):
    dest1 = Destination.objects.all()
    return render(request, 'party_info.html', {'dest1': dest1})


def index(request):
    dest1 = Destination.objects.all()
    return render(request, 'index.html', {'dest1': dest1})


def voting(request):
    dest1 = Destination.objects.all()
    return render(request, 'voting.html', {'dest1': dest1})


def index1(request):
    return render(request, 'index.html')


def home(request):
    return render(request, 'base.html')


def Election(request):
    return render(request, 'Election.html')


def help(request):
    return render(request, 'help.html')
