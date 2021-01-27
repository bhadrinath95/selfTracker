from django.contrib import admin
from .models import CycleTracker, ActionPlanner, Reminder, Preparation, Interview

# Register your models here.
class CycleTrackerDisplay(admin.ModelAdmin):
    list_display=('user','date','start_time','time_taken','distance','max_speed','average_speed','calories')
admin.site.register(CycleTracker, CycleTrackerDisplay)
class ActionPlannerDisplay(admin.ModelAdmin):
    list_display=('user','date','title','description')
admin.site.register(ActionPlanner, ActionPlannerDisplay)
class ReminderDisplay(admin.ModelAdmin):
    list_display=('user','date','title','description','status')
admin.site.register(Reminder, ReminderDisplay)
class PreparationDisplay(admin.ModelAdmin):
    list_display=('user','date','title','description')
admin.site.register(Preparation, PreparationDisplay)
class InterviewDisplay(admin.ModelAdmin):
    list_display=('user','date','company','role','round','description','status')
admin.site.register(Interview, InterviewDisplay)