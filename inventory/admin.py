from django.contrib import admin
from .models import Customer, ItemType, IndividualItem, Category, Group

admin.site.register(Customer)
admin.site.register(ItemType)
admin.site.register(IndividualItem)
admin.site.register(Category)
admin.site.register(Group)