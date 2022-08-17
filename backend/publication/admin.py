from django.contrib import admin

from .models import PublicationModel, CategoryModel

# Register your models here.
admin.site.register(PublicationModel)
admin.site.register(CategoryModel)