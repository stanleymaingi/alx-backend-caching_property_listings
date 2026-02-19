# properties/views.py
from django.http import JsonResponse
from django.views.decorators.cache import cache_page
from .models import Property


@cache_page(60 * 15)  # Cache for 15 minutes
def property_list(request):
    properties = Property.objects.all().values('id', 'title', 'price', 'description')  # include fields you want
    data = list(properties)  # convert QuerySet to list of dicts
    return JsonResponse({'data': data})
