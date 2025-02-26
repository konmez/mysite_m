from django.contrib import admin # type: ignore

# Register your models here.
from .models import Profile # type: ignore

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'photo']
    raw_id_fields = ['user']