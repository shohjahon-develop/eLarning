from django.contrib import admin
from .models import Bot,Add,Web,Papular,Expert,Instruct,Aexp,Exp,Cour,Team,Courses

# Register your models here.
admin.site.register(Add)
admin.site.register(Web)
admin.site.register(Papular)
admin.site.register(Expert)
admin.site.register(Exp)
admin.site.register(Aexp)
admin.site.register(Cour)
admin.site.register(Instruct)
@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":('name',)}
@admin.register(Courses)
class CourseAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":('name',)}


















