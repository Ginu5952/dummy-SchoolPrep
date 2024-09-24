from django.shortcuts import render


def holiday_list(request):
    return render(request, 'parent/holiday_list.html') 


def extra_curricular_timetable(request):
    return render(request, 'parent/extra_curricular_timetable.html')