from django.contrib import admin
from app1.models import Job,Application

class job_admin(admin.ModelAdmin):
    list_display=['title','description','recruiter']
admin.site.register(Job,job_admin)

class application_admin(admin.ModelAdmin):
    list_display=['user','job','resume','status','updated_at']
admin.site.register(Application,application_admin)



