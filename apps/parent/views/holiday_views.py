from django.shortcuts import render


def holiday_list(request):
    return render(request, 'parent/holiday_list.html') 