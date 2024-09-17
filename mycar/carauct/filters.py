from django_filters.rest_framework import FilterSet
from .models import Car

class CarFilter(FilterSet):
    class Meta:
        model = Car
        fields = {
            'category': ['exact'],
            'Car_Make': ['exact'],
            'model': ['exact'],
            'price': ['gt', 'lt'],
            'year': ['gt', 'lt'],
        }