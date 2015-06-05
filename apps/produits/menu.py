from menus.base import NavigationNode, Modifier
from menus.menu_pool import menu_pool
from django.utils.translation import ugettext_lazy as _
from cms.menu_bases import CMSAttachMenu
from produits.models import SubCategory, Category

class SubCategoryMenu(CMSAttachMenu):

	name = _("Swivels")

	def get_nodes(self, request):
		nodes = []
		cat = request.current_page
		for category in Category.objects.filter(associated_page__reverse_id = "swivels_page"):
			nodes.append(NavigationNode(category.title, "/swivels/"+ category.slug + '/', category.id*154332345, None, None, {'is_extending' : True}))
			for subcategory in SubCategory.objects.filter(category__id = category.id):
				nodes.append(NavigationNode(subcategory.title, "/swivels/"+ category.slug + '/' + subcategory.slug, subcategory.id, category.id*154332345))
		return nodes

#class SubCategoryMenu2(CMSAttachMenu):

#	name = _("aSwivel Products")
#	def get_nodes(self, request):
#		nodes = []
#		cat = request.current_page
#		for category in Category.objects.filter(associated_page__reverse_id = "swivelproduct"):
#			nodes.append(NavigationNode(category.title, "/produits/"+ category.slug + '/', category.id*154332345, None ,None, {'is_extending' : True}))
#			for subcategory in SubCategory.objects.filter(category__id = category.id):
#				nodes.append(NavigationNode(subcategory.title, "/produits/"+ category.slug + '/' + subcategory.slug, subcategory.id, category.id*154332345))
#		return nodes
#menu_pool.register_menu(SubCategoryMenu2)
menu_pool.register_menu(SubCategoryMenu)

class NavExtender(Modifier):
    def modify(self, request, nodes, namespace, root_id, post_cut, breadcrumb):
        if post_cut:
            return nodes
        nodes = sorted(nodes, key=lambda n: n.attr.get("is_extending", None), reverse=True)
        exts = []
        # rearrange the parent relations
        home = None
        for node in nodes:
            if node.attr.get("is_home", False):
                home = node
            extenders = node.attr.get("navigation_extenders", None)
            if extenders:
                for ext in extenders:
                    if not ext in exts:
                        exts.append(ext)
                    for extnode in nodes:
                        if extnode.namespace == ext and not extnode.parent_id:# if home has nav extenders but home is not visible
                            if node.attr.get("is_home", False) and not node.visible:
                                extnode.parent_id = None
                                extnode.parent_namespace = None
                                extnode.parent = None
                            else:
                                extnode.parent_id = node.id
                                extnode.parent_namespace = node.namespace
                                extnode.parent = node
                                node.children.append(extnode)
        removed = []
        # find all not assigned nodes
        for menu in menu_pool.menus.items():
            if hasattr(menu[1], 'cms_enabled') and menu[1].cms_enabled and not menu[0] in exts:
                for node in nodes:
                    if node.namespace == menu[0]:
                        removed.append(node)
        if breadcrumb:  
            # if breadcrumb and home not in navigation add node
            if breadcrumb and home and not home.visible:
                home.visible = True
                if request.path == home.get_absolute_url():
                    home.selected = True
                else:
                    home.selected = False
        # remove all nodes that are nav_extenders and not assigned 
        for node in removed:
            nodes.remove(node)
        return nodes   
menu_pool.register_modifier(NavExtender)

