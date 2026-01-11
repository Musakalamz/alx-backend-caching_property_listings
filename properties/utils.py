from django.core.cache import cache
from .models import Property

def get_all_properties():
    all_properties = cache.get('all_properties')
    if not all_properties:
        all_properties = Property.objects.all()
        cache.set('all_properties', all_properties, 3600)
    return all_properties
