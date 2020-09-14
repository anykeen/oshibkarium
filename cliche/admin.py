from django.contrib import admin
from cliche.models import Cliche
from django.apps import apps


class ClicheAdmin(admin.ModelAdmin):
    list_display = ['cliche', 'rating', 'author']
    readonly_fields = ['author', 'rating']

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.author = request.user.profile
        super(ClicheAdmin, self).save_model(request, obj, form, change)

admin.site.register(Cliche, ClicheAdmin)