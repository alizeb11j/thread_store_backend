from django.contrib import admin

from .models import Item

class MyModelAdmin(admin.ModelAdmin):
    pass

admin.site.register(Item, MyModelAdmin)
