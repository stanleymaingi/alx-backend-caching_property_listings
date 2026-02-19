# properties/utils.py
from django.core.cache import cache # type: ignore
from .models import Property

def get_all_properties():
    # Try to get cached queryset
    properties = cache.get('all_properties')
    if properties is None:
        # Cache miss, fetch from database
        properties = list(Property.objects.all().values('id', 'title', 'price', 'description'))
        # Store in Redis for 1 hour (3600 seconds)
        cache.set('all_properties', properties, 3600)
    return properties
