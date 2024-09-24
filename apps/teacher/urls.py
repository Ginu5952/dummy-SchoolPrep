from django.urls import path
from . import views

app_name = 'teacher-urls'
urlpatterns = [


    path('registration/', views.teacher_list, name='teacher_list_create'),
    path('list/leave/requests/', views.teacher_leave_list, name='teacher-leave-list'),
    path('leave/status/update/<int:leave_id>/', views.update_leave_status, name='update-leave-status'), 
    
]    