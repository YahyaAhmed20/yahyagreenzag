from django.db import models
from django.utils.html import mark_safe

class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    
    # الصورة الرئيسية (تظهر في project_list)
    main_image = models.ImageField(
        upload_to='projects/main/',
        blank=True,
        null=True,
        help_text="الصورة الظاهرة في صفحة القائمة"
    )
    
    # حقول الترتيب
    is_featured = models.BooleanField(
        default=False,
        help_text="يظهر المشروع دايمًا في الأعلى"
    )
    priority = models.IntegerField(
        default=0,
        help_text="أرقام أقل تظهر في الأعلى (مثلاً: 1 هو الأعلى)"
    )

    class Meta:
        ordering = ['-is_featured', 'priority', '-id']

    def __str__(self):
        return self.name

    def main_image_tag(self):
        if self.main_image:
            return mark_safe(f'<img src="{self.main_image.url}" width="100" height="100" />')
        return "لا توجد صورة"
    main_image_tag.short_description = 'الصورة الرئيسية'

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name='gallery_images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='projects/gallery/')  # الصور الإضافية فقط

    def __str__(self):
        return f"{self.project.name} - Image {self.id}"

    def image_tag(self):
        if self.image:
            return mark_safe(f'<img src="{self.image.url}" width="100" height="100" />')
        return "لا توجد صورة"
    image_tag.short_description = 'الصورة'