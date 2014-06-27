from django.contrib import admin
from .models import PostModel


class PostModelAdmin(admin.ModelAdmin):
    pass

admin.site.register(PostModel, PostModelAdmin)
