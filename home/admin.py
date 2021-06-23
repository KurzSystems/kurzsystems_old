from django.contrib import admin
from .models import NotifyEmail, Video
# Register your models here.

class EmailListAdmin(admin.ModelAdmin):
    list_display = ('email', 'date_added',)

admin.site.register(NotifyEmail, EmailListAdmin)
admin.site.register(Video)
