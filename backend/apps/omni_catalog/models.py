from django.db import models

# Create your models here.
class Omnibus(models.Model):
    id = models.IntegerField(primary_key=True)
    digital_id = models.IntegerField()
    title = models.CharField(max_length=255)
    issue_number = models.IntegerField()
    variant_description = models.TextField(blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    modified = models.DateTimeField()
    isbn = models.CharField(max_length=20)
    upc = models.CharField(max_length=20)
    diamond_code = models.CharField(max_length=20)
    ean = models.CharField(max_length=20)
    issn = models.CharField(max_length=20, blank=True, null=True)
    format = models.CharField(max_length=100)
    page_count = models.IntegerField()
    text_objects = models.JSONField(default=dict)  # Requires Django 3.1 or higher
    resource_uri = models.URLField()
    urls = models.JSONField(default=dict)
    series = models.JSONField(default=dict)  # Extracted from 'series' field
    variants = models.JSONField(default=dict)
    collections = models.JSONField(default=dict)
    collected_issues = models.JSONField(default=dict)
    dates = models.JSONField(default=dict)
    prices = models.JSONField(default=dict)  # Extracted from 'prices' field
    thumbnail = models.JSONField(default=dict)  # Extracted from 'thumbnail' field
    images = models.JSONField(default=dict)
    creators = models.JSONField(default=dict)
    characters = models.JSONField(default=dict)
    stories = models.JSONField(default=dict)
    events = models.JSONField(default=dict)

    class Meta:
        verbose_name_plural = "Marvel Omnibuses"
        # unique_together = ('isbn', 'upc')
