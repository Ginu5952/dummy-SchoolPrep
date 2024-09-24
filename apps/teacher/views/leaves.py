from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from apps.parent.models.leave import Leave
from apps.parent.serializer.leave import LeaveSerializer
from rest_framework import serializers
from rest_framework import status


class LeaveStatusUpdateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Leave
        fields = ['status']  

    def update(self, instance, validated_data):
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance

@api_view(['GET'])
@permission_classes([IsAuthenticated])  
def teacher_leave_list(request):
    
    leaves = Leave.objects.all()  
    serializer = LeaveSerializer(leaves, many=True)
    return Response(serializer.data)


@api_view(['PATCH'])  
@permission_classes([IsAuthenticated])  
def update_leave_status(request, leave_id):
    
    try:
        leave = Leave.objects.get(id=leave_id)
    except Leave.DoesNotExist:
        return Response({'error': 'Leave request not found.'}, status=status.HTTP_404_NOT_FOUND)
    
    
    leave.status = request.data.get('status', leave.status)
    leave.save()

  
    serializer = LeaveSerializer(leave)
    return Response(serializer.data)