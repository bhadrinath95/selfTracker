from django.contrib import admin
from .models import CycleTracker, ActionPlanner

# Register your models here.
class CycleTrackerDisplay(admin.ModelAdmin):
    list_display=('user','date','start_time','time_taken','distance','max_speed','average_speed','calories')
admin.site.register(CycleTracker, CycleTrackerDisplay)
class ActionPlannerDisplay(admin.ModelAdmin):
    list_display=('user','date','title','description')
admin.site.register(ActionPlanner, ActionPlannerDisplay)