from django.urls import path
from .views import Home,Register,Cycle,Action,ToDo,Prepare,InterviewView
urlpatterns=[
    path('cycle',Cycle.as_view(),name='cycle'),
    path('action',Action.as_view(),name='action'),
    path('todo',ToDo.as_view(),name='todo'),
    path('prepare',Prepare.as_view(),name='prepare'),
    path('interview',InterviewView.as_view(),name='interview'),
    path('accounts/register',Register.as_view()),
    path('',Home.as_view(),name='home'),
]