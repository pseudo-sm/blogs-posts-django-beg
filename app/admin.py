from django.contrib import admin
from .models import Post,Author
# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    
    list_display = ('name','email','category','is_active','gender')
    search_fields = ('name','email')
    list_filter = ('category','is_active','gender')

admin.site.register(Post)
admin.site.register(Author,AuthorAdmin)