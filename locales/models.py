from django.db import models
from django.utils.translation import gettext_lazy as _


class CountryModel(models.Model):
    """
    :format_meta
        postal:
            postal_format:
            postal_name:

    """
    id = models.CharField(max_length=2, primary_key=True, auto_created=False)
    iso2 = models.CharField(max_length=2, null=False, blank=False, unique=True)
    iso3 = models.CharField(max_length=3, null=True, blank=True, unique=True)
    iso_number = models.CharField(max_length=8, null=True, blank=True)
    name = models.CharField(max_length=127, null=False, blank=False)
    native_name = models.CharField(max_length=127, null=True, blank=False)
    capital = models.CharField(max_length=127, null=True, blank=True)
    currency = models.TextField(serialize=False, null=True, blank=True)
    regions = models.TextField(serialize=False, null=True, blank=True)
    timezone = models.TextField(serialize=False, null=True, blank=True)
    calling_code = models.CharField(max_length=16, null=True, blank=True)
    subdivisions = models.TextField(serialize=False, null=True, blank=False)
    languages = models.TextField(serialize=False, null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    tld = models.TextField(serialize=False, null=True, blank=True)
    format_meta = models.TextField(serialize=False, null=True, blank=True)
    attribute_meta = models.TextField(null=True, serialize=False, default=None)

    class Meta:
        app_label = "locales"
        db_table = "%s_countries" % app_label
        verbose_name = _("country")
        verbose_name_plural = _("countries")

    def __unicode__(self):
        return self.name


class LanguageModel(models.Model):
    """

    """
    iso2 = models.CharField(max_length=2, null=False, blank=False)
    iso3 = models.CharField(max_length=2, null=True, blank=True)
    name = models.CharField(max_length=127, null=True, blank=True)
    native_name = models.CharField(max_length=127, null=True, blank=True)
    is_rtl = models.BooleanField(null=False, default=False)
    format_meta = models.TextField(serialize=False, null=True)

    class Meta:
        app_label = "locales"
        db_table = "%s_languages" % app_label
        verbose_name = _("language")
        verbose_name_plural = _("languages")

    def __unicode__(self):
        return self.name