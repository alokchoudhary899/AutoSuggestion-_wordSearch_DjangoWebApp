from django.db import models

# Create your models here.

class SearchElements(models.Model):
    words = models.CharField(blank=True, null=True, max_length=50)
    Use_count = models.IntegerField('count of words used', blank=False, default=None)

