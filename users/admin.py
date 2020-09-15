from django.contrib import admin
from users.models import Profile

class ProfileAdmin(admin.ModelAdmin):
    readonly_fields = ['user', 'current', 'finished']
    exclude = ['voted']

admin.site.register(Profile, ProfileAdmin)

