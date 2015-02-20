from django.contrib import admin

from planning.models import Batch, Placement


class BatchAdmin(admin.ModelAdmin):
    list_display = ('compound', 'start', 'end', 'state',)
    list_filter = ('compound', 'start', 'state', )


class PlacementAdmin(admin.ModelAdmin):
    pass


admin.site.register(Batch, BatchAdmin)
admin.site.register(Placement, PlacementAdmin)
