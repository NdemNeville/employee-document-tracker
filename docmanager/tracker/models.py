from django.db import models
from django.core.validators import FileExtensionValidator
from datetime import datetime, timedelta
# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Document(models.Model):
    STATUS_CHOICES = [
        ('Pending','Pending'),
        ('Submitted','Submitted'),
        ('Expired','Expired'),
    ]
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    submission_date = models.DateTimeField(null=True, auto_now_add=True)
    expiry_date = models.DateTimeField(blank=True, null=True)
    file = models.FileField(upload_to='documents/', validators=[FileExtensionValidator(['pdf'])], null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.expiry_date:
            # Set expiry_date to 1 year after submission_date
            if self.submission_date:
                self.expiry_date = self.submission_date + timedelta(days=365)
            else:
            # If submission_date not set yet (new object), use now()
                self.expiry_date = datetime.now() + timedelta(days=365)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} - {self.employee.name}"

