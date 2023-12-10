# Generated by Django 4.2.6 on 2023-12-10 03:32

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Omnibus",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("digital_id", models.IntegerField()),
                ("title", models.CharField(max_length=255)),
                ("issue_number", models.IntegerField()),
                ("variant_description", models.TextField(blank=True)),
                ("description", models.TextField(blank=True)),
                ("modified", models.DateTimeField()),
                ("isbn", models.CharField(max_length=20)),
                ("upc", models.CharField(max_length=20)),
                ("diamond_code", models.CharField(max_length=20)),
                ("ean", models.CharField(max_length=20)),
                ("issn", models.CharField(blank=True, max_length=20)),
                ("omnibus_format", models.CharField(max_length=100)),
                ("page_count", models.IntegerField()),
                ("text_objects", models.JSONField()),
                ("resource_uri", models.URLField()),
                ("urls", models.JSONField()),
                ("series_name", models.CharField(max_length=255)),
                ("onsale_date", models.DateField()),
                ("foc_date", models.DateField()),
                ("print_price", models.DecimalField(decimal_places=2, max_digits=6)),
                ("thumbnail_path", models.URLField()),
                ("images", models.JSONField()),
                ("creators", models.JSONField()),
                ("characters", models.JSONField()),
                ("stories", models.JSONField()),
                ("events", models.JSONField()),
            ],
            options={
                "verbose_name_plural": "Marvel Omnibuses",
                "unique_together": {("isbn", "upc")},
            },
        ),
    ]