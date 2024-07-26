from django.urls import path
from .views import *
urlpatterns=[
    path('',home),
    path('addstudents/',addstudents,name='add_student'),
    path('allstudents/',allstudents,name='all_student'),
    path('allstudents/delete/<int:id>',delete_student,name='delete_student'),
    path('allstudentss/update/<int:id>',update_student,name='update_student')
    
]