from django.contrib import admin
from .models import Category, Post

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
     readonly_fields = ('created', 'updated')
     
class PostAdmin(admin.ModelAdmin):
     readonly_fields = ('created', 'updated')
     list_display = ('title', 'autho','published', 'post_categories')
     ordering = ('autho', 'published')
     search_fields = ('title', 'content', 'autho__username', 'categories__name')
     date_hierarchy = 'published'
     list_filter = ('title', 'autho__username', 'categories__name')
     
     def post_categories(self, obj):
          return ", ".join([ c.name for c in obj.categories.all().order_by('name')  ])
     
     post_categories.short_description = "Categorías"
     
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)

