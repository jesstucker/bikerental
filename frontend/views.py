from django.shortcuts import render, HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from inventory.models import *

def index(request):
	# html = "HI"
	return render(request, 'index.html')

def catalog(request):

	return render(request, 
				'catalog.html', 
				{
					'category' : Category.objects.all(),
					'group' : Group.objects.all(),
					'item_type': ItemType.objects.all(),
					'individual_item': IndividualItem.objects.all(),
				}
	)

def get_groups(request):
    data = Group.objects.all()
    
    return HttpResponse(json.dumps(data), content_type='application/json')
