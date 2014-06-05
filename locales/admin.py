from django.contrib import admin
from .models import (CountryModel, LanguageModel)


class CountryModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'native_name', 'iso2')


class LanguageModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'native_name', 'iso2')


admin.site.register(CountryModel, CountryModelAdmin)
admin.site.register(LanguageModel, LanguageModelAdmin)