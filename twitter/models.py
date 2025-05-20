from django.db import models
from wagtail.admin.panels import FieldPanel

class TwitterAccount(models.Model):
    name = models.CharField(max_length=100)
    api_key = models.CharField(max_length=100)
    api_secret = models.CharField(max_length=100)
    access_token = models.CharField(max_length=100)
    access_token_secret = models.CharField(max_length=100)

    panels = [
        FieldPanel('name'),
        FieldPanel('api_key'),
        FieldPanel('api_secret'),
        FieldPanel('access_token'),
        FieldPanel('access_token_secret'),
    ]

    def __str__(self):
        return self.name
