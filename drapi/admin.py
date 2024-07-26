from django.contrib import admin
from . import models
# Register your models here.
@admin.register(models.Aiquest)
class AiquestAdmin(admin.ModelAdmin):
    list_display=['id','teacher_name','course_name','course_duration','seat']