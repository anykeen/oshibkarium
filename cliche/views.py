from django.shortcuts import render
from .models import Cliche

def cliche(request):
    cliche = Cliche.objects.order_by('rating')
    return render(request, 'cliche/index.html', {'cliche': cliche} )
