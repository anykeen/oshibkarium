from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Card, Page

# slug в моделях — CharField без проверки; адреса с другими символами
# маршрут <slug:slug> всё равно не откроет, в карту их не берём.
SLUG_RE = r'^[-a-zA-Z0-9_]+$'


class IndexSitemap(Sitemap):
    priority = 1.0

    def items(self):
        return ['index']

    def location(self, item):
        return reverse(item)


class CardSitemap(Sitemap):
    priority = 0.8

    def items(self):
        return Card.objects.filter(published=True, slug__regex=SLUG_RE).order_by('id')

    def location(self, card):
        return reverse('card_detail', args=[card.slug])


class PageSitemap(Sitemap):
    priority = 0.5

    def items(self):
        return Page.objects.filter(slug__regex=SLUG_RE).order_by('id')

    def location(self, page):
        return reverse('page', args=[page.slug])


sitemaps = {
    'index': IndexSitemap,
    'cards': CardSitemap,
    'pages': PageSitemap,
}
