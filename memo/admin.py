from django.contrib import admin
from .models import Memo

# Register your models here.
class Memo_admin(admin.ModelAdmin):
    list_display = ('title', 'description', 'content', 'image', 'video', 'created_at', 'updated_at')
    search_fields = ('title', 'description')

admin.site.register(Memo, Memo_admin)