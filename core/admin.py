from django.contrib import admin
from core.models import Card, Category, Relationship

class RelatedInline(admin.TabularInline):
    model = Relationship
    list_display = ['title']
    can_delete = False
    fk_name = 'parent'
    extra = 4

class CardAdmin(admin.ModelAdmin):
    inlines = [RelatedInline]

admin.site.register(Card, CardAdmin)
admin.site.register(Category)
