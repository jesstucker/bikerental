"""bikerental URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from frontend import views as frontend_views
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from inventory.models import Customer, Category, Group, ItemType, IndividualItem

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'name', 'notes')
class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer



class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('id','description')
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    category = serializers.CharField(source='catg', read_only=True)
    # category = serializers.RelatedField(source='catg')
    catg_id = serializers.SerializerMethodField('id_me')

    def id_me(self, Group):
        return Group.catg.id 
    class Meta:
        model = Group        
        fields = ('id', 'description', 'category', 'catg_id',
            )
class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer



class ItemTypeSerializer(serializers.HyperlinkedModelSerializer):
    group_id = serializers.SerializerMethodField('id_me')
    def id_me(self, ItemType):
        return ItemType.group.id 

    class Meta:
        model = ItemType
        fields = ('id', 'name', 'group', 'cost_per_hour', 
            'cost_per_day', 'image', 'group_id')
class ItemTypeViewSet(viewsets.ModelViewSet):
    queryset = ItemType.objects.all()
    serializer_class = ItemTypeSerializer




router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'customer', CustomerViewSet)
router.register(r'category', CategoryViewSet)
router.register(r'group', GroupViewSet)
router.register(r'item-type', ItemTypeViewSet)






urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', frontend_views.index),
    url(r'^catalog', frontend_views.catalog),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]
