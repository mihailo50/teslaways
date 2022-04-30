from django_filters.rest_framework import filterset
from django_filters.rest_framework import filters
from teslaways.models import destination, news, podtip
from django import forms


class DestinationFilter(filterset.FilterSet):
    tip = filters.MultipleChoiceFilter(choices=destination.MY_CHOICES,lookup_expr='icontains', widget=forms.CheckboxSelectMultiple)
    zone = filters.AllValuesMultipleFilter('zone__name',lookup_expr='icontains', widget=forms.CheckboxSelectMultiple)
    podtip = filters.AllValuesFilter('pod_tip__name')

    class Meta:
        model = destination.Destination
        fields = ('tip','zone', 'podtip')

class NewsFilter(filterset.FilterSet):

    zone = filters.AllValuesFilter('zone__name', lookup_expr='iexact')
    class Meta:
        model = news.News
        fields = ('zone',)

class PodTipDestinationFilter(filterset.FilterSet):
    podtip = filters.AllValuesFilter('name')

    class Meta:
        model = podtip.Podtip
        fields = ('podtip', )
