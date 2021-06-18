from django.contrib import admin
from .models import NotifyEmail
# Register your models here.

class EmailListAdmin(admin.ModelAdmin):
    list_display = ('email', 'date_added',)

admin.site.register(NotifyEmail, EmailListAdmin)
