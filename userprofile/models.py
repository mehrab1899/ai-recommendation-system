from django.db import models
from users.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    full_name = models.CharField(max_length=255, blank=True, null=True)
    profile_picture = models.ImageField(upload_to="profile_pics/", blank=True, null=True)
    current_role = models.CharField(max_length=255, blank=True, null=True)
    years_of_experience = models.IntegerField(blank=True, null=True)
    skills = models.JSONField(blank=True, null=True)  # Example: ["Python", "React.js"]
    preferred_industries = models.CharField(max_length=255, blank=True, null=True)
    education_level = models.CharField(
        max_length=50, choices=[("Bachelors", "Bachelors"), ("Masters", "Masters"), ("PhD", "PhD")], blank=True, null=True
    )
    certifications = models.JSONField(blank=True, null=True)  # Example: ["AWS Certified", "Google Data Analytics"]
    projects = models.TextField(blank=True, null=True)
    resume = models.FileField(upload_to="resumes/", blank=True, null=True)
    career_goals = models.TextField(blank=True, null=True)
    learning_preferences = models.CharField(
        max_length=50,
        choices=[("Self-paced", "Self-paced"), ("Bootcamps", "Bootcamps"), ("University courses", "University courses")],
        blank=True,
        null=True,
    )
    soft_skills = models.JSONField(blank=True, null=True)  # Example: ["Problem-solving", "Communication"]
    work_preference = models.CharField(
        max_length=50, choices=[("Remote", "Remote"), ("Hybrid", "Hybrid"), ("On-site", "On-site")], blank=True, null=True
    )
    job_search_status = models.CharField(
        max_length=50,
        choices=[("Open to work", "Open to work"), ("Just exploring", "Just exploring"), ("Actively applying", "Actively applying")],
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.user.email} - Profile"
