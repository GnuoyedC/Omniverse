from django.db import models

# Create your models here.
class Omnibus(models.Model):
    id = models.IntegerField(primary_key=True)
    digital_id = models.IntegerField()
    title = models.CharField(max_length=255)
    issue_number = models.IntegerField()
    variant_description = models.TextField(blank=True)
    description = models.TextField(blank=True)
    modified = models.DateTimeField()
    isbn = models.CharField(max_length=20)
    upc = models.CharField(max_length=20)
    diamond_code = models.CharField(max_length=20)
    ean = models.CharField(max_length=20)
    issn = models.CharField(max_length=20, blank=True)
    omnibus_format = models.CharField(max_length=100)
    page_count = models.IntegerField()
    text_objects = models.JSONField()  # Requires Django 3.1 or higher
    resource_uri = models.URLField()
    urls = models.JSONField()
    series_name = models.CharField(max_length=255)  # Extracted from 'series' field
    onsale_date = models.DateField()  # Extracted from 'dates' field
    foc_date = models.DateField()  # Extracted from 'dates' field
    print_price = models.DecimalField(max_digits=6, decimal_places=2)  # Extracted from 'prices' field
    thumbnail_path = models.URLField()  # Extracted from 'thumbnail' field
    images = models.JSONField()
    creators = models.JSONField()
    characters = models.JSONField()
    stories = models.JSONField()
    events = models.JSONField()

    class Meta:
        verbose_name_plural = "Marvel Omnibuses"
        unique_together = ('isbn', 'upc')
