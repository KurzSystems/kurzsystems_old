from django.db import models

from wagtail.core.models import Page


class HomePage(Page):
    pass

class NotifyEmail(models.Model):
    email = models.EmailField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
