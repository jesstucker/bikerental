from django.db import models
from django.db.models import Q
from django.core.exceptions import ValidationError
from inventory import models as inventory_models
from django.contrib.auth.models import User
from time import strftime
from datetime import timedelta, datetime
from django.utils import timezone
from collections import namedtuple

HOUR = timedelta(hours=1)



class Reservation(models.Model):
	def __str__(self):
		return f'{self.customer}, {self.item}. \
		{timezone.localtime(self.begins).strftime("%m/%d %H:%M")}\
		 –\
		{timezone.localtime(self.ends).strftime("%m/%d %H:%M")}'
	item = models.ForeignKey(inventory_models.IndividualItem)
	customer = models.ForeignKey(inventory_models.Customer)
	begins = models.DateTimeField()
	ends = models.DateTimeField()

	def clean(self):

		Range = namedtuple('Range', ['start', 'end'])
		r2 = Range(start=self.begins, end=self.ends)
		res_this_item = Reservation.objects.filter(item__id=self.item.id)

		for res in res_this_item:
			r1 = Range(start=res.begins, end=res.ends)
			latest_start = max(r1.start, r2.start)
			earliest_end = min(r1.end, r2.end)
			overlap = (earliest_end - latest_start).days + 1
			if overlap > 0:
				raise ValidationError(f"This conflicts with a prior reservation date.\
					{res.customer} : {timezone.localtime(res.begins).strftime('%m/%d %H:%M')}\
					-{timezone.localtime(res.ends).strftime('%m/%d %H:%M')}")

		if self.begins > self.ends:
			raise ValidationError("This is time travel")


	def save(self, *args, **kwargs):
		self.ends += HOUR
		self.full_clean()
		return super(Reservation, self).save(*args, **kwargs)