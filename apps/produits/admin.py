from django.contrib.admin import site, ModelAdmin, StackedInline
from produits.models import Category, SubCategory, Product
from multilingual.admin import MultilingualModelAdmin

class SubcategoryInline(StackedInline):
	model = SubCategory
	extra = 1
class CategoryAdmin(MultilingualModelAdmin):
	inlines = [ SubcategoryInline, ]
	list_display = ('title',)
	search_fields = ['title']
class ProductInline(StackedInline):
	model = Product
	extra = 1
class SubCategoryAdmin(MultilingualModelAdmin):
	inlines = [ ProductInline, ]
	list_display = ('title', 'category')
	search_fields = ['title']
class ProductAdmin(ModelAdmin):
	list_display = ('part_no', 'subcategory', 'category')
	search_fields = ['part_no']
	list_filter = ('subcategory', 'subcategory__category')
    

site.register(Category, CategoryAdmin)
site.register(SubCategory, SubCategoryAdmin)
site.register(Product, ProductAdmin)
