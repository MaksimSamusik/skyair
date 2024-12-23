from django.contrib import admin

from .models import Planes, Profile


class PlanesAdmin(admin.ModelAdmin):
    list_display = ('flight', 'departure_date', 'arrival_date', 'time_create', 'time_update', 'is_published')
    list_display_links = ('flight', )
    search_fields = ('flight', )


admin.site.register(Planes, PlanesAdmin)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'profile_picture']