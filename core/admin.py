from django.contrib import admin
from core.models import Card, Category, Relationship, Page, Example, Zalupa

def all_card(modeladmin, reguest, queryset):
    for qs in queryset:
        print(qs.title)

def complete_card(modeladmin, reguest, queryset):
    queryset.update(published=True)
complete_card.short_description = 'Опубликовать'

def incomplete_card(modeladmin, reguest, queryset):
    queryset.update(published=False)
incomplete_card.short_description = 'Снять с публикации'

class RelatedInline(admin.TabularInline):
    model = Relationship
    list_display = ['title']
    can_delete = False
    fk_name = 'parent'
    extra = 1

class Exrel(admin.TabularInline):
    model = Example
    extra = 1

class Zalrel(admin.TabularInline):
    model = Zalupa
    extra = 1

class CardAdmin(admin.ModelAdmin):
    inlines = [Exrel, RelatedInline, Zalrel]
    readonly_fields = ['clarity_pos', 'clarity_neg']
    list_display = ['title', 'published', 'category', 'clarity_pos', 'clarity_neg']
    actions = [all_card, complete_card, incomplete_card]


admin.site.register(Card, CardAdmin)
admin.site.register(Category)
admin.site.register(Page)
