from django_filters import FilterSet
from .models import Property

class PropertyFilter(FilterSet):
    class Meta:
        model = Property
        fields = {
            'property_type': ['exact'],
            'rule': ['exact'],
            'stars': ['gt', 'lt'],
            'price': ['gt', 'lt'],
        }