from django.urls import path
from .views import Home,Register,Cycle,Action,ToDo,Prepare,InterviewView,export_cycle_xls,export_action_xls,export_todo_xls,export_prepare_xls,export_interview_xls
urlpatterns=[
    path('cycle',Cycle.as_view(),name='cycle'),
    path('action',Action.as_view(),name='action'),
    path('todo',ToDo.as_view(),name='todo'),
    path('prepare',Prepare.as_view(),name='prepare'),
    path('interview',InterviewView.as_view(),name='interview'),
    path('accounts/register',Register.as_view()),
    path('export/xls/cycle',export_cycle_xls.as_view(), name='export_cycle_xls'),
    path('export/xls/action',export_action_xls.as_view(), name='export_action_xls'),
    path('export/xls/todo',export_todo_xls.as_view(), name='export_todo_xls'),
    path('export/xls/prepare',export_prepare_xls.as_view(), name='export_prepare_xls'),
    path('export/xls/interview',export_interview_xls.as_view(), name='export_interview_xls'),
    path('',Home.as_view(),name='home'),
]