from django.shortcuts import render, get_object_or_404
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.core.validators import validate_email
from django.http import Http404, HttpResponse, HttpResponseBadRequest
from .models import Card, Category, Page
from django.views.decorators.csrf import csrf_exempt
from django.db.models import F

def index(request):
    index = Page.objects.get(slug = '/')
    cats = Category.objects.order_by('num').prefetch_related('cards')
    return render(request, 'core/index.html', {'page': index, 'cats': cats} )

def card(request, slug):
    # Неопубликованные карточки видят только сотрудники (для предпросмотра).
    cards = Card.objects.all() if request.user.is_staff else Card.objects.filter(published=True)
    card = get_object_or_404(cards, slug=slug)
    return render(request, 'core/card_detail.html', {'card': card})

def page(request, slug):
    page = get_object_or_404(Page, slug=slug)
    return render(request, 'core/page.html', {'page': page})

def robots_txt(request):
    lines = [
        'User-agent: *',
        'Disallow: /admin/',
        'Disallow: /accounts/',
        'Disallow: /api/',
        '',
        'Sitemap: ' + request.build_absolute_uri('/sitemap.xml'),
    ]
    return HttpResponse('\n'.join(lines) + '\n', content_type='text/plain; charset=utf-8')

def card_from_post(request):
    """Карточка по id из POST; кривой или пустой id — 404, а не 500."""
    try:
        card_id = int(request.POST.get('id', ''))
    except ValueError:
        raise Http404
    return get_object_or_404(Card, id=card_id)

@csrf_exempt
def editor_request(request):
    name = request.POST.get('name', '').strip()
    email = request.POST.get('email', '').strip()
    try:
        validate_email(email)
    except ValidationError:
        return HttpResponseBadRequest()

    message = 'Запрос редактора от ' + name + ' с email ' + email
    send_mail('Запрос редактора', message, None, ['timur@anykeen.ru',])

    return HttpResponse(status=204)

@csrf_exempt
def clarity_pos(request):
    card = card_from_post(request)
    Card.objects.filter(id=card.id).update(clarity_pos=F('clarity_pos') + 1)

    return HttpResponse(status=204)

@csrf_exempt
def clarity_neg(request):
    card = card_from_post(request)
    Card.objects.filter(id=card.id).update(clarity_neg=F('clarity_neg') + 1)

    return HttpResponse(status=204)
