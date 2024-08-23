import datetime
from django.shortcuts import render
# from .models import -MODELS-

def homepage(request):
    context = {
        'datetime': datetime.datetime.now,
    }
    return render(request, 'homepage.html', context=context)
