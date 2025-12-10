from django.db import models
from django.utils.html import mark_safe
from cloudinary.models import CloudinaryField

class Project(models.Model):
    name = models.CharField(max_length=200, verbose_name="اسم المشروع")
    description = models.TextField(blank=True, verbose_name="الوصف")
    
    # ✅ الصورة الرئيسية — باستخدام CloudinaryField
    main_image = CloudinaryField(
    folder='projects/main/',
    blank=True,
    null=True,
    help_text="الصورة الظاهرة في صفحة القائمة",
    verbose_name="الصورة الرئيسية"
)
    
    # حقول الترتيب
    is_featured = models.BooleanField(
        default=False,
        help_text="يظهر المشروع دايمًا في الأعلى",
        verbose_name="مميز؟"
    )
    priority = models.IntegerField(
        default=0,
        help_text="أرقام أقل = ظهور أعلى (مثل: 1 هو الأعلى)",
        verbose_name="أولوية الظهور"
    )

    class Meta:
        ordering = ['-is_featured', 'priority', '-id']
        verbose_name = "مشروع"
        verbose_name_plural = "المشاريع"

    def __str__(self):
        return self.name

    # ✅ دالة العرض في الـ Admin — مدعومة لـ Cloudinary
    def main_image_tag(self):
        if self.main_image:
            # Cloudinary يعطيك URL مباشر — نستخدم `url` attribute
            return mark_safe(
                f'<img src="{self.main_image.url}" '
                f'style="width:100px; height:100px; object-fit:cover; border-radius:4px;" />'
            )
        return "لا توجد صورة"
    main_image_tag.short_description = 'معاينة الصورة'

class ProjectImage(models.Model):
    project = models.ForeignKey(
        Project, 
        related_name='gallery_images', 
        on_delete=models.CASCADE,
        verbose_name="المشروع"
    )
    # ✅ الصور الإضافية — أيضًا Cloudinary
    image = CloudinaryField(
    folder='projects/gallery/',
    verbose_name="الصورة"
)

    class Meta:
        verbose_name = "صورة إضافية"
        verbose_name_plural = "معرض الصور"

    def __str__(self):
        return f"{self.project.name} - Image {self.id}"

    def image_tag(self):
        if self.image:
            return mark_safe(
                f'<img src="{self.image.url}" '
                f'style="width:100px; height:100px; object-fit:cover; border-radius:4px;" />'
            )
        return "لا توجد صورة"
    image_tag.short_description = 'معاينة'