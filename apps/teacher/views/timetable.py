from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from apps.teacher.models.timetable import Timetable,Subject
from apps.teacher.serializer.timetable import TimetableResponseSerializer
from django.shortcuts import get_object_or_404
from apps.teacher.models.teacher import Class




@api_view(['GET', 'POST'])
def timetable_view(request,class_id):
   
  
    if request.method == 'GET':
        class_obj = get_object_or_404(Class, id=class_id)
        serializer = TimetableResponseSerializer(class_obj)
        return Response(serializer.data)

   
    elif request.method == 'POST':
        class_obj = get_object_or_404(Class, id=class_id)
        data = request.data.get('timetable')

        if not data:
            return Response({"error": "Invalid data"}, status=status.HTTP_400_BAD_REQUEST)

     
        for entry in data:
            day = entry.get('day')
            schedule = entry.get('schedule', [])

            for session in schedule:
                subject_name = session.get('subject')
                teacher_name = session.get('teacher')
                start_time = session.get('start_time')
                end_time = session.get('end_time')

              
                subject = Subject.objects.filter(name=subject_name, class_id=class_obj).first()
                if not subject:
                    return Response({"error": f"Subject '{subject_name}' not found in class."}, status=status.HTTP_404_NOT_FOUND)

             
                Timetable.objects.create(
                    class_id=class_obj,
                    day=day,
                    subject=subject,
                    start_time=start_time,
                    end_time=end_time
                )

        return Response({"message": "Timetable successfully created."}, status=status.HTTP_201_CREATED)
