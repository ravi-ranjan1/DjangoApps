from django.contrib import admin
from .models import Blog


@admin.register(Blog)
class BlogAdminModel(admin.ModelAdmin):
    list_display = ['id','title','content']


