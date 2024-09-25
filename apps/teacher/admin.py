from django.contrib import admin
from apps.teacher.models.teacher import Teacher,Attendance



class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id','username', 'first_name', 'last_name', 'gender', 'class_name')

    def username(self, obj):
        return obj.user.username  

    def first_name(self, obj):
        return obj.user.first_name  

    def last_name(self, obj):
        return obj.user.last_name  
    def class_name(self, obj):
        return obj.class_id.class_name  

    username.admin_order_field = 'user__username'  
    first_name.admin_order_field = 'user__first_name'  
    last_name.admin_order_field = 'user__last_name'  
    class_name.admin_order_field = 'class_id__class_name' 
    
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'teacher', 'get_class_name','date', 'is_present')
    
    
    list_filter = ('date', 'is_present', 'teacher')
    search_fields = ('student__first_name', 'student__last_name', 'teacher__first_name', 'teacher__last_name')
    
    def get_class_name(self, obj):
        return obj.student.class_id.class_name  

    get_class_name.short_description = 'Class Name' 
    
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Attendance,AttendanceAdmin)
