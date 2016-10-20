from django.contrib import admin
# set up automated slug creation
#imort your model
from collection.models import Thing


class ThingAdmin(admin.ModelAdmin):
    model=Thing
    list_display= ('name', 'description',)
    prepopulated_fields = {'slug': ('name',)}

# and register it
admin.site.register(Thing, ThingAdmin)
# Register your models here.
