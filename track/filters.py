from .models import Claim
import django_filters

class ClaimFilter(django_filters.FilterSet):
    class Meta:
        model = Claim
        fields = ['CLAIMNO', 'TEXT',  ]