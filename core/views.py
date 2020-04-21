from django.shortcuts import render, get_object_or_404, render_to_response
from django.core.mail import send_mail
from .models import Card, Category, Page
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt

def index(request):
    index = Page.objects.get(slug = '/')
    cats = Category.objects.order_by('num').prefetch_related('cards')
    return render(request, 'core/index.html', {'page': index, 'cats': cats} )

def card(request, slug):
    card = get_object_or_404(Card, slug=slug)
    return render(request, 'core/card_detail.html', {'card': card})

def page(request, slug):
    page = get_object_or_404(Page, slug=slug)
    return render(request, 'core/page.html', {'page': page})

def handler404(request, *args, **argv):
    response = render_to_response('404.html', {}, context_instance=RequestContext(request))
    response.status_code = 404
    return response

@csrf_exempt
def editor_request(request):
    name = request.POST.get('name')
    email = request.POST.get('email')

    message = str('Запрос редактора от ' + name + ' с email ' + email )
    send_mail('Запрос редактора', message, 'from@mail.me', ['timur@anykeen.ru',])

    return render(request, 'core/page.html')