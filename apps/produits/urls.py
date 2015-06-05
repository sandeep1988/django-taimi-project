from django.conf.urls.defaults import *

urlpatterns = patterns('produits.views',
    url(r'listinfo/$', "listProductInfo", name="productInfo"),
    url(r'addinfo/(?P<pid>.+)/$', "addProductInfo", name="productInfo"),
    url(r'reminfo/(?P<pid>.+)/$', "removeProductInfo", name="productInfo"),
	url(r'recherche/', "search", name="recherche"),
	url(r'(?P<cat>.+)/(?P<subcat>.+)/$', "getProducts", name="subcategorie"),
	url(r'(?P<cat>.+)/$', "getSubCats", name="subcategorie"),
    url(r'$', "getIndex", name="getIndex"),
)
