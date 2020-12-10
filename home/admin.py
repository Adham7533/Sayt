from django.contrib import admin
from .models import *

# Register your models here.

class PostImageInline(admin.TabularInline):
    model = ImagesPost
    extre =5

class PostAdmin(admin.ModelAdmin):
    list_display =['title','author','image_tag']
    readonly_fields = ('image_tag',)
    inlines = [PostImageInline]

class SettingAdmin(admin.ModelAdmin):
    list_display = ['title','company','update_at']

admin.site.register(Setting,SettingAdmin)
admin.site.register(Post,PostAdmin)
admin.site.register(ImagesPost)