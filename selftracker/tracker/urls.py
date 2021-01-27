from django.urls import path
from .views import Home,Register,Cycle
urlpatterns=[
    path('cycle',Cycle.as_view(),name='cycle'),
    path('accounts/register',Register.as_view()),
    path('',Home.as_view(),name='home'),
]