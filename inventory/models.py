from django.db import models
from django.core.validators import URLValidator, RegexValidator



class Customer(models.Model):
    """
    Test :D
    """
    def __str__(self):
        return '%s' % (self.name)
    name = models.CharField(max_length=100)
    notes = models.TextField()
    address = models.TextField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',\
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=15, blank=True)
    email = models.EmailField()

class Category(models.Model):
    def __str__(self):
        return '%s' % (self.description)
    class Meta:
        verbose_name_plural = "Categories"
    description = models.CharField(max_length=100)
    

class Group(models.Model):
    def __str__(self):
        return '%s' % (self.description)
    description = models.CharField(max_length=100)
    catg = models.ForeignKey(Category, null=True)

class ItemType(models.Model):
    def __str__(self):
        return '%s' % (self.name)
    name = models.CharField(max_length=100)
    group = models.ForeignKey(Group)
    cost_per_hour = models.DecimalField(max_digits=6, decimal_places=2)
    cost_per_day = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.TextField(validators=[URLValidator()])
    
class IndividualItem(models.Model):
    def __str__(self):
        return '%s' % (self.item_type)
    barcode = models.IntegerField()
    item_type = models.ForeignKey(ItemType)
    customer = models.ForeignKey(Customer, blank=True, null=True)

