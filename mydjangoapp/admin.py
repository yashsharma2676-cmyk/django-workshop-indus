from django.contrib import admin

# Register your models here.
from . models import student,  Category, Product

admin.site.register(student)
admin.site.register(Category)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'price')
    list_filter = ('category',)
    search_fields = ('title',)

#customize the admin panel
admin.site.site_header = "MyProject Admin"
admin.site.site_title = "MyProject Admin Portal"
admin.site.index_title = "Welcome to MyProject Admin Dashboard"