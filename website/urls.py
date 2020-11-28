from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('employee/api',views.employeelist.as_view(),name='employee'),
]