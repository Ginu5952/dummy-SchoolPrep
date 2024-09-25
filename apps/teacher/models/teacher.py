from django.contrib.auth.models import User
from django.db import models
from apps.parent.models.parent import Class
from apps.student.models.student import Student
from django.utils import timezone
from django.core.exceptions import ValidationError



class Teacher(models.Model):
    
    user = models.OneToOneField("auth.User", on_delete=models.CASCADE) 
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE)  
    gender = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female')])
    
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
    
    
class Attendance(models.Model):
    
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE) 
    student = models.ForeignKey(Student, on_delete=models.CASCADE)  
    date = models.DateField(default=timezone.now)
    is_present = models.BooleanField(default=True)
    

    class Meta:
        unique_together = ('student', 'date') 
        
    def clean(self):
       
        if self.date > timezone.now().date():
            raise ValidationError("Attendance cannot be marked for future dates.")    

    def __str__(self):
        return f"{self.student.username} - {self.date} - {'Present' if self.is_present else 'Absent'}"    