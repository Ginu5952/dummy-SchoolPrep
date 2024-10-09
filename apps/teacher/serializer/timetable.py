
from rest_framework import serializers
from apps.teacher.models.timetable import Timetable
from apps.teacher.models.teacher import Class
from datetime import datetime

class SubjectScheduleSerializer(serializers.ModelSerializer):
    subject = serializers.CharField(source='subject.name')
    teacher = serializers.CharField(source='subject.teacher.user.first_name')

    class Meta:
        model = Timetable
        fields = ['subject', 'start_time', 'end_time', 'teacher']
        

class DayScheduleSerializer(serializers.Serializer):
    day = serializers.CharField()
    schedule = SubjectScheduleSerializer(many=True)
    
    
class TimetableResponseSerializer(serializers.ModelSerializer):
    academic_year = serializers.SerializerMethodField()
    timetable = serializers.SerializerMethodField()

    class Meta:
        model = Class
        fields = ['class_name', 'academic_year', 'grade', 'timetable']
        
        
    def validate_start_time(self, value):
        return self._convert_to_24_hour_format(value)

    def validate_end_time(self, value):
        return self._convert_to_24_hour_format(value)

    def _convert_to_24_hour_format(self, time_str):
        try:
            # Assuming the input is in 'HH:MM AM/PM' format
            return datetime.strptime(time_str, '%I:%M %p').time()
        except ValueError:
            raise serializers.ValidationError("Time format must be in 'HH:MM AM/PM'")

    def get_academic_year(self, obj):
        return f"{obj.academic_year_start}-{obj.academic_year_end}"

    def get_timetable(self, obj):
        timetable_entries = Timetable.objects.filter(class_id=obj)
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        timetable_by_day = []

        for day in days:
            day_entries = timetable_entries.filter(day=day)
            if day_entries:
                timetable_by_day.append({
                    'day': day,
                    'schedule': SubjectScheduleSerializer(day_entries, many=True).data
                })

        return timetable_by_day

    