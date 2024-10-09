from django.urls import path
from . import views


app_name = 'parent-urls'
urlpatterns = [


    path('registration/', views.parent_list, name='parent_list_create'),
    path('student/info/', views.parent_student_info, name='parent_student_info'),
    path('apply/leave/', views.parent_leave_list_create, name='apply_leave'), 
    path('holiday/list/', views.holiday_list, name='holiday-list'),
    path('extracurricular/timetable/', views.extra_curricular_timetable, name='extra_curricular_timetable'), 
    path('verify-email/<str:uidb64>/<str:token>/', views.verify_email, name='verify-email'),
    path('profile/', views.parent_profile, name='parent-profile'),
]    