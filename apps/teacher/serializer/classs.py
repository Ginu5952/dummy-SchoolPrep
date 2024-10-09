from rest_framework import serializers
from apps.teacher.models.teacher import Class


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ['id', 'class_name', 'academic_year_start', 'academic_year_end', 'grade']

    def __str__(self) -> str:
        return super().__str__()