
# Register your models here.



from django.contrib import admin

from import_export.admin import ExportActionModelAdmin, ImportExportMixin, ImportMixin
from import_export.resources import ModelResource

from .models import Claim


#admin.site.register(Book)



class ClaimResource(ModelResource):

    class Meta:
        model = Claim

class ClaimAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = ClaimResource
admin.site.register(Claim, ClaimAdmin)


