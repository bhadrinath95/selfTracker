from django.contrib import admin
from .models import CycleTracker

# Register your models here.
class CycleTrackerDisplay(admin.ModelAdmin):
    list_display=('user','date','start_time','time_taken','distance','max_speed','average_speed','calories')
admin.site.register(CycleTracker, CycleTrackerDisplay)