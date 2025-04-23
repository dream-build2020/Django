from django.contrib import admin
from polls.models import Job

# Register your models here.

class JobAdmin(admin.ModelAdmin):
    exclude = ('creator', 'created_date', 'modified_date')
    list_display = ('job_type', 'job_name', 'job_city')

    def save_model(self, request, obj, form, change):
        obj.creator = request.user
        super().save_model(request, obj, form, change)

admin.site.register(Job, JobAdmin)