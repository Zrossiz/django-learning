from django.contrib import admin
from django.contrib.admin import ModelAdmin

from women.models import Women


# Register your models here.
@admin.register(Women)
class BookAdmin(ModelAdmin):
    pass