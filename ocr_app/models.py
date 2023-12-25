from django.db import models
class OCRRecord(models.Model):
    identification_number = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    date_of_issue = models.DateField()
    date_of_expiry = models.DateField()
    # Add other fields as needed

    def __str__(self):
        return self.identification_number

# Create your models here.

