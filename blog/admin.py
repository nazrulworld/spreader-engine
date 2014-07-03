from django.contrib import admin
import models

admin.site.register(models.PostCategoryModel)
admin.site.register(models.PostModel)
admin.site.register(models.CommentModel)
admin.site.register(models.TagModel)

