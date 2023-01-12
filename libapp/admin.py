from django.contrib import admin
from libapp.models import Tickit
# Register your models here.
# admin.site.register(Tickit)

class TickitAdmin(admin.ModelAdmin):

    list_display=['btitle','cat','Aname','is_deleted']
    list_filter=['cat','Aname','is_deleted']

admin.site.register(Tickit,TickitAdmin)    