from django.db import models

class Textbook(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    edition = models.CharField(max_length=50, blank=True, null=True)
    condition = models.CharField(max_length=50)  # e.g., 'Like New', 'Written', 'Old'
    course_code = models.CharField(max_length=50)
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} ({self.course_code})"