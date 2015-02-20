from django.contrib import admin

from mptt.admin import MPTTModelAdmin

from resources.models import ResourceBase, Resource, Compound


class ResourceBaseAdmin(MPTTModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


class ResourceAdmin(MPTTModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


class CompoundAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(ResourceBase, ResourceBaseAdmin)
admin.site.register(Resource, ResourceAdmin)
admin.site.register(Compound, CompoundAdmin)
