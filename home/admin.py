from django.contrib import admin

from .models import Recipe, Type, Complexity, Tags, Type_of_kitchen

# Register your models here.
admin.site.register(Recipe)
admin.site.register(Type)
admin.site.register(Complexity)
admin.site.register(Tags)
admin.site.register(Type_of_kitchen)