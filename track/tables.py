import django_tables2 as tables
from .models import Track
import itertools
from django_tables2.utils import A

class TrackTable(tables.Table):
    
    #id = tables.Column()
    #id  = tables.LinkColumn('note', text=lambda record: record.id, args=[A('claimNumber')])
    #claimId  = tables.LinkColumn('note', text=lambda record: record.claimId, args=[A('claimNumber')])

    def __init__(self, *args, **kwargs):
            super(TrackTable, self).__init__(*args, **kwargs)
            self.counter = itertools.count()
    
    #def render_id(self, value):
    #    return '<a href="/%s">%s</a>' % (value , value)

            
    class Meta:
        model = Track
        #fields = ('customer', 'claimNumber', 'indicators', 'reviewed', 'noteText')
        #sequence = ('customer', 'claimNumber', 'indicators', 'reviewed', 'noteText')
        template_name = 'django_tables2/bootstrap4.html'

