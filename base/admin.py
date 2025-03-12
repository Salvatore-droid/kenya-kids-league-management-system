from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Campus)
admin.site.register(HighSchool)
admin.site.register(ManageCourse)
admin.site.register(CampusLeveling)
admin.site.register(HighschoolLeveling)
admin.site.register(MiddleschoolLeveling)
admin.site.register(CampusStudent)
admin.site.register(HighschoolStudent)
admin.site.register(MiddleschoolStudent)
admin.site.register(CampusStudentResult)
admin.site.register(HighschoolStudentResult)

