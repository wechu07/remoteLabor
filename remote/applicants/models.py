from django.db import models

class Applicant(models.Model):
    user_id = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    profile = models.TextField()
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')])
    skills = models.CharField(max_length=255)
    resume = models.FileField(upload_to='resumes/')
    contact_email = models.EmailField()
    contact_number = models.CharField(max_length=20)
    jobs_completed = models.PositiveIntegerField(default=0)
