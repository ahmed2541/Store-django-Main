from re import I
from django.contrib import admin
from .models import Item,Category, ItemImage,Item_Alternative,Item_Accessories
# Register your models here.
admin.site.register(Item)
admin.site.register(ItemImage)
admin.site.register(Category)
admin.site.register(Item_Alternative)
admin.site.register(Item_Accessories)
