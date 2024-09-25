from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from apps.student.models.student import Student
from apps.teacher.models.teacher import Attendance
from apps.teacher.serializer.attendance import AttendanceSerializer
from rest_framework.permissions import IsAuthenticated
from apps.teacher.models.teacher import Teacher


@api_view(['GET'])
@permission_classes([IsAuthenticated])  
def attendance_list(request):
   
    try:
        
        teacher = Teacher.objects.get(user=request.user)  
    except Teacher.DoesNotExist:
        return Response({'error': 'Teacher not found.'}, status=status.HTTP_404_NOT_FOUND)

    
    today = timezone.now().date()

   
    attendance_records = Attendance.objects.filter(
        student__class_id=teacher.class_id,
        date=today
    )

    
    serializer = AttendanceSerializer(attendance_records, many=True)
    
    
    if not attendance_records.exists():
        return Response({'message': 'No attendance records found for today.'}, status=status.HTTP_200_OK)

    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['PATCH']) 
@permission_classes([IsAuthenticated])  
def update_attendance_status(request, student_id):
    
    
    try:
       
        teacher = Teacher.objects.get(user=request.user)  
    except Teacher.DoesNotExist:
        return Response({'error': 'Teacher not found.'}, status=status.HTTP_404_NOT_FOUND)

    try:
       
        student = Student.objects.get(id=student_id, class_id=teacher.class_id) 
    except Student.DoesNotExist:
        return Response({'error': 'Student not found or not in the teacher\'s class.'}, status=status.HTTP_404_NOT_FOUND)

    
    today = timezone.now().date()

    
    attendance, created = Attendance.objects.get_or_create(
        student=student,
        date=today,
        defaults={
            'is_present': request.data.get('is_present', True),  
            'teacher': teacher  
        }
    )

   
    if not created:
        attendance.is_present = request.data.get('is_present', attendance.is_present)
        attendance.teacher = teacher  
        attendance.save()

    
    serializer = AttendanceSerializer(attendance)
    return Response(serializer.data, status=status.HTTP_200_OK)
