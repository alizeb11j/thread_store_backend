from django.contrib import admin

from .models import ImagesItem

class MyModelAdmin(admin.ModelAdmin):
    pass

admin.site.register(ImagesItem, MyModelAdmin)
