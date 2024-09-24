from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from apps.parent.models.leave import Leave
from apps.parent.serializer.leave import LeaveSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])  
def teacher_leave_list(request):
    
    leaves = Leave.objects.all()  
    serializer = LeaveSerializer(leaves, many=True)
    return Response(serializer.data)
