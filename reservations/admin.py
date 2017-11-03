from django.contrib import admin
from reservations.models import Reservation

admin.site.register(Reservation)

# @admin.register(Reservation)
# class TabDisplayReservation(admin.ModelAdmin):
# 	change_list_template = 'admin/tab_display_reservation.html'
# 	date_heirarchy = 'created'

# 	def changelist_view(self, request, extra_context=None):
# 		reservations = Reservation.objects.all()
# 		# response = super().changelist_view(
# 		# 	request,
# 		# 	extra_context=extra_context,
# 		# )
# 		# try:
# 		# 	qs = response.context_data['cl'].queryset
# 		# except (AttributeError, KeyError):
# 		# 	return response
		
# 		# metrics = {
# 		# 	'total': Count('id'),
# 		# 	'total_sales': Sum('price'),
# 		# }
# 		# response.context_data['summary'] = list(
# 		# 	qs
# 			# .values('sale__category__name')
# 			# .annotate(**metrics)
# 			# .order_by('-total_sales')
# 		# )
		
# 		return response