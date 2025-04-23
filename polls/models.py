from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.

JobTypes = [
    (0, "技术类"),
    (1, "产品类")
]

Cities = [
    (0, "北京"),
    (1, "深圳"),
    (2, "上海")
]

class Job(models.Model):
    job_type = models.SmallIntegerField(blank=False, choices=JobTypes , verbose_name='Job type')
    job_name = models.CharField(max_length=255, blank=False, verbose_name='Job name')
    job_city = models.SmallIntegerField(blank=False, choices=Cities , verbose_name='Job city')
    job_responsibility = models.TextField(blank=False, max_length=1024, verbose_name='Job responsibility')
    job_requirements = models.TextField(blank=False, max_length=1024, verbose_name='Job requirements')
    creator = models.ForeignKey(User, verbose_name='Creator',null=True, on_delete=models.SET_NULL)
    created_date = models.DateTimeField(verbose_name='Created date', default=datetime.now)
    modified_date = models.DateTimeField(verbose_name='Modified date', default=datetime.now)
