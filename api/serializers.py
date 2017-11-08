from django.contrib.auth.models import User

from rest_framework import routers, serializers, viewsets
from inventory.models import Customer, Category, Group, ItemType, IndividualItem

#Getting a dern token
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token
from django.dispatch import receiver
from django.conf import settings

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer




class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'name', 'notes')
class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id','description')
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class GroupSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='catg', read_only=True)
    # category = serializers.RelatedField(source='catg')
    catg_id = serializers.SerializerMethodField('id_me')

    def id_me(self, Group):
        return Group.catg.id 
    class Meta:
        model = Group        
        fields = ('id', 'description', 'category', 'catg', 'catg_id',
            )
class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer



class ItemTypeSerializer(serializers.ModelSerializer):
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


from reservations.models import BikeReservationDatesReport
from rest_framework.views import APIView
from rest_framework.response import Response
class BikeDatesReportView(APIView):
    def get(self, request):
        response = Response(BikeReservationDatesReport.get_all_dates())
        return response



router = routers.DefaultRouter()

router.register(r'users', UserViewSet)
router.register(r'customer', CustomerViewSet)
router.register(r'category', CategoryViewSet)
router.register(r'group', GroupViewSet)
router.register(r'item-type', ItemTypeViewSet)

from reservations.models import Reservation
from rest_framework import generics

class ReservationSerializer(serializers.ModelSerializer):
    daterange = serializers.ReadOnlyField(source='reservation_daterange')
    class Meta:
        model = Reservation
        fields = '__all__'

class ReservationList(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def get_queryset(self):
        queryset = Reservation.objects.all()
        item = self.request.query_params.get('item', None)
        begin = self.request.query_params.get('begin', None)
        end = self.request.query_params.get('end', None)
        daterange = self.request.query_params.get('daterange', None)


        if item is not None:
            queryset = queryset.filter(item=item)
        if end is not None:
            queryset = queryset.filter(ends__lte=end)
        if begin is not None:
            queryset = queryset.filter(begins__gte=begin)
        if daterange is not None:
            queryset = queryset.filter(reservation_daterange=daterange)
        return queryset

router.register(r'reservations', ReservationList)
