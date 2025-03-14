from django.contrib import admin
from django.utils.html import format_html
from .models import *

# Register your models here.
@admin.register(Campus)
class CampusAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    list_filter = ('location',)
    search_fields = ('name', 'location')


@admin.register(HighSchool)
class HighSchoolAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    list_filter = ('location',)
    search_fields = ('name', 'location')


@admin.register(ManageCourse)
class ManageCourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('name',)


@admin.register(CampusLeveling)
class CampusLevelingAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('name',)


@admin.register(HighschoolLeveling)
class HighschoolLevelingAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('name',)


@admin.register(MiddleschoolLeveling)
class MiddleschoolLevelingAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('name',)


class CampusStudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'course', 'school', 'display_image')
    list_filter = ('course', 'school')
    search_fields = ('name', 'bio')
    exclude = ('user',)  # Remove the user selection option
    readonly_fields = ('image_preview',)  # Add 'image_preview' to readonly_fields

    def display_image(self, obj):
        if obj.imageURL:  # Use the imageURL property
            return format_html('<img src="{}" width="50" height="50" style="border-radius: 50%; object-fit:cover;" />', obj.imageURL)
        return "No Image"

    def image_preview(self, obj):
        if obj.imageURL:  # Use the imageURL property
            return format_html('<img src="{}" width="150" height="150" style="border-radius: 10px; object-fit:cover;" />', obj.imageURL)
        return "No Image"

    display_image.short_description = 'Image'  # Column header for list view
    image_preview.short_description = 'Image Preview'  # Field label for detail view

admin.site.register(CampusStudent, CampusStudentAdmin)



@admin.register(HighschoolStudent)
class HighschoolStudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'level', 'school', 'image_preview')
    list_filter = ('level', 'school')
    search_fields = ('name', 'bio')
    exclude = ('user',)  # Remove the user selection option

    def image_preview(self, obj):
        if obj.imageURL:
            return format_html('<img src="{}" width="50" height="50" style="border-radius: 50%;" />', obj.imageURL)
        return "No Image"
    image_preview.short_description = 'Image Preview'


@admin.register(MiddleschoolStudent)
class MiddleschoolStudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'grade', 'image_preview')
    list_filter = ('grade',)
    search_fields = ('name', 'bio')
    exclude = ('user',)  # Remove the user selection option

    def image_preview(self, obj):
        if obj.imageURL:
            return format_html('<img src="{}" width="50" height="50" style="border-radius: 50%;" />', obj.imageURL)
        return "No Image"
    image_preview.short_description = 'Image Preview'


@admin.register(CampusStudentResult)
class CampusStudentResultAdmin(admin.ModelAdmin):
    list_display = ('campus', 'test', 'exam', 'total_score', 'created_at')
    list_filter = ('campus__course', 'campus__school', 'created_at')
    search_fields = ('campus__name',)

    def total_score(self, obj):
        return obj.test + obj.exam
    total_score.short_description = 'Total Score'


@admin.register(HighschoolStudentResult)
class HighschoolStudentResultAdmin(admin.ModelAdmin):
    list_display = ('high', 'test', 'exam', 'total_score', 'created_at')
    list_filter = ('high__level', 'high__school', 'created_at')
    search_fields = ('high__name',)

    def total_score(self, obj):
        return obj.test + obj.exam
    total_score.short_description = 'Total Score'