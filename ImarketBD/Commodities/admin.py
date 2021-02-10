from django.contrib import admin
from .models import commodities_import, commodities_info, commodities_production


admin.site.register(commodities_info)
admin.site.register(commodities_production)
admin.site.register(commodities_import)
