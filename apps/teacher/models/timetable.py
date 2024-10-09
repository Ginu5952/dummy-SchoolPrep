from django.db import models
from apps.teacher.models.teacher import Class,Teacher



class Subject(models.Model):
    
    name = models.CharField(max_length=100)
    class_id = models.ForeignKey(Class, related_name='subjects', on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, related_name='subjects', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - Class: {self.class_id.class_name} - Teacher: {self.teacher.user.first_name} {self.teacher.user.last_name}"
    

class Timetable(models.Model):
    
    class_id = models.ForeignKey(Class, related_name='timetable', on_delete=models.CASCADE)
    
    day = models.CharField(max_length=10, choices=[
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday')
    ])
    
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()    
    
    def __str__(self):
        return f"{self.class_id.class_name} - {self.day} - {self.subject.name}"