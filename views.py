from django.shortcuts import render
from . models import Bikers_Choice


def index(request):
    bikersChoice = Bikers_Choice.objects.all

    context = {
        'items': bikersChoice
    }
    return render(request, 'Bikers_Choice/index.html', context)
