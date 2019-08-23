from django.utils import timezone

from django.contrib.auth.models import User
from django.db import models


def cover_upload_path(instance, filename):
    return '/'.join(['socialize', str(instance.id), filename])


class Project(models.Model):
    proj_name = models.CharField(max_length=250, null=False)
    proj_link = models.CharField(max_length=100, blank=True)
    proj_description = models.TextField()
    proj_start_date = models.DateField(null=False)
    proj_end_date = models.DateField(default=timezone.now)
    proj_status = models.BooleanField(default=False)
    proj_GOC = models.CharField(max_length=250)

    def __str__(self):
        return '%s' % self.proj_name


class Employee(User):
    emp_id = models.IntegerField(primary_key=True)
    dob = models.DateField(null=False)
    location = models.CharField(max_length=200, blank=False, null=False)
    profile_pic = models.ImageField(upload_to=cover_upload_path, default='socialize/profile_pic_empty.png')
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=False, null=False)
    about = models.TextField(null=True)
    interest = models.CharField(max_length=200, null=True)
    project = models.ManyToManyField(Project)


class myEmployee(Employee, models.Model):
    class Meta:
        proxy = True
        ordering = ["emp_id"]


class Department(models.Model):
    empl = models.ForeignKey(Employee, on_delete=models.CASCADE)
