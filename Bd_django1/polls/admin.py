from django.contrib import admin
from .models import Course, Client, Teacher, Dgroup


# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id_cor', 'name', 'price')
    list_display_links = ('id_cor', 'name', 'price')
    search_fields = ['id_cor']


class ClientAdmin(admin.ModelAdmin):
    list_display = ('id_cl', 'lastname', 'firstname', 'middlename')
    list_display_links = ('id_cl', 'lastname', 'firstname', 'middlename')
    search_fields = ['id_cl']


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id_t', 'lastname', 'firstname', 'middlename')
    list_display_links = ('id_t', 'lastname', 'firstname', 'middlename')
    search_fields = ['id_t']

class DgroupAdmin(admin.ModelAdmin):
    list_display = ('id_g', 'id_cl', 'id_cor', 'id_t')
    list_display_links = ('id_g', 'id_cl', 'id_cor', 'id_t')
    search_fields = ['id_g']


admin.site.register(Course, CourseAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Dgroup, DgroupAdmin)
