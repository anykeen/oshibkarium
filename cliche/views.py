from django.shortcuts import render, get_object_or_404, render_to_response
from .models import Cliche
from django.views.decorators.csrf import csrf_exempt
from django.db.models import F
from django.contrib.postgres.search import SearchQuery, SearchVector

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

@csrf_exempt
def add_cliche(request):
    cliche = request.POST.get('cliche')
    author = request.user.profile
    vector = SearchVector('cliche')
    query = SearchQuery(cliche)
    data = {
        'already_exist': Cliche.objects.annotate(search=vector).filter(search=query)
    }
    if data['already_exist']:
        data['error_message'] = 'A cliche already exists.'
        Cliche.objects.create(cliche=cliche, author=author, status="declined")
    else:
        Cliche.objects.create(cliche=cliche, author=author, status="pending")
    
    return JsonResponse(data)