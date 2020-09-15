from django.shortcuts import render, get_object_or_404, render_to_response
from .models import Cliche
from django.views.decorators.csrf import csrf_exempt
from django.db.models import F

def cliche(request):
    cliche = Cliche.objects.order_by('rating')
    return render(request, 'cliche/index.html', {'cliche': cliche} )

@csrf_exempt
def pos_vote(request):
    cliche_id = request.POST.get('id')
    cliche = get_object_or_404(Cliche, id=cliche_id)
    Cliche.objects.filter(id=cliche_id).update(rating=F('rating') + 1)
    request.user.profile.voted.add(cliche)
    request.user.profile.save()

    return render(request, 'cliche/index.html')

@csrf_exempt
def neg_vote(request):
    cliche_id = request.POST.get('id')
    cliche = get_object_or_404(Cliche, id=cliche_id)
    Cliche.objects.filter(id=cliche_id).update(rating=F('rating') - 1)
    request.user.profile.voted.add(cliche)
    request.user.profile.save()

    return render(request, 'cliche/index.html')
