from django.contrib import admin
from .models import Project, ProjectImage

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_featured', 'priority', 'main_image_tag']
    list_editable = ['is_featured', 'priority']
    list_filter = ['is_featured']
    search_fields = ['name']
    inlines = [ProjectImageInline]
    fields = ['name', 'description', 'main_image', 'is_featured', 'priority']  # تحديد الحقول الظاهرة

# @admin.register(ProjectImage)
# class ProjectImageAdmin(admin.ModelAdmin):
#     list_display = ['project', 'image_tag']