from django.contrib import admin
from . import models

class VINFilter(admin.SimpleListFilter):
    title = 'Search VIN'
    parameter_name = 'vin'

    def lookups(self, request, model_admin):
        return []

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(object_id__vin__icontains=self.value())
        return queryset

@admin.register(models.Trackers)
class TrackersAdmin(admin.ModelAdmin):
    # Añadimos el filtro personalizado
    list_filter = (VINFilter,)
    search_fields = ('tracker_id', 'object_id__vin')  # Añade búsqueda en VIN

    # Visualización de campos en la lista de la admin
    list_display = ('oid', 'tracker_id', 'provider', 'type', 'vehicle_type', 'start_date', 'end_date')


#admin.site.register(models.Trackers)
admin.site.register(models.Trips)
admin.site.register(models.Companies)