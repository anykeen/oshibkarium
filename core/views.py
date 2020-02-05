from django.shortcuts import render, get_object_or_404
from .models import Card, Category

def index(request):
    cats = Category.objects.all()
    cards = Card.objects.all().order_by('-category')
    return render(request, 'core/card_list.html', {'cats': cats, 'cards': cards})

def card(request, slug):
    card = get_object_or_404(Card, slug=slug)
    return render(request, 'core/card_detail.html', {'card': card})
