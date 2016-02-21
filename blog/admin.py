from django.contrib import admin

# Register your models here.
from .models import Post
from .models import Genre
from .models import Category, Product

from mptt.admin import MPTTModelAdmin
from django_mptt_admin.admin import DjangoMpttAdmin

'''
class GenreAdmin(admin.ModelAdmin):
#    fields = ['name', 'parent_name', 'budget', 'date_of_budget']
    fieldsets = [
        (None, {'fields': ['name']}),
        ('Info Genre', {'fields': ['parent', 'budget']}),
        ]

    list_display = ('name', 'parent', 'budget')
#    list_filter = ['parent_name', 'type', 'level']
    search_fields = ['name', 'budget']
'''
class GenreAdmin(DjangoMpttAdmin):
#    fields = ['name', 'parent_name', 'budget', 'date_of_budget']

    fieldsets = [
        (None, {'fields': ['name']}),
        ('Info Genre', {'fields': ['parent', 'budget']}),
        ]

    list_display = ('name', 'parent', 'budget')
    list_filter = ['name', 'parent', 'budget']
    search_fields = ['name', 'parent', 'budget']


admin.site.register(Post)
admin.site.register(Genre, GenreAdmin)



#############################################################################################"


# Register your models here.
#class CategoryAdmin(MPTTModelAdmin):
class CategoryAdmin(DjangoMpttAdmin):
#    fields = ['name', 'description', 'amount', 'parent']

    fieldsets = [
        (None, {'fields': ['name']}),
        ('Info Catégorie', {'fields': ['parent', 'description', 'amount']}),
        ]

    list_display = ('name', 'amount','parent',)
    search_fields = ['name', 'amount', ]

    list_filter = ('parent',)

#    mptt_level_indent = 20

admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    ordering = ('code',)
    fieldsets = [
        (None, {'fields': ['code', 'stocks', 'category']}),
		#(None, {'fields': ['code', 'stocks', 'image', 'category']}),
        (None, {'fields': ['name', 'description',]}),
        ('Prices', {'fields': ['priceAustria'], 'classes': ['grp-collapse  grp-closed']}),
    ]
    # change_list_template = 'admin/product_change_list.html'
    list_display = ('code', 'name', 'category')
    search_fields = ['code']

    list_filter = ('name',)


admin.site.register(Product, ProductAdmin)