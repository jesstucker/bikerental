from django.db import models
from django.core.validators import URLValidator

class Customer(models.Model):
	def __str__(self):
		return '%s' % (self.name)
	name = models.CharField(max_length=100)
	notes = models.TextField()

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
	catg = models.ForeignKey(Category)

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
		return '%s' % (self.barcode)
	barcode = models.IntegerField()
	item_type = models.ForeignKey(ItemType)
	customer = models.ForeignKey(Customer, blank=True, null=True)

