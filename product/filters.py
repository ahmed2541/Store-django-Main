
from .models import Item
import django_filters

class ItemFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    # manufacturer__name = django_filters.CharFilter(lookup_expr='contains')
    # description = django_filters.CharFilter(lookup_expr='iconatains')
    # discount_price = django_filters.NumberFilter()
    # discount_price__gt = django_filters.NumberFilter(field_name='discount_price', lookup_expr='gt')
    # discount_price__lt = django_filters.NumberFilter(field_name='discount_price', lookup_expr='lt')
    # price = django_filters.NumberFilter()
    # price__gt = django_filters.NumberFilter(field_name='price', lookup_expr='gt')
    # price__lt = django_filters.NumberFilter(field_name='price', lookup_expr='lt')
    class Meta :
        model = Item
        fields = ['name']