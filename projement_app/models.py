from django.db import models
from django.core.validators import RegexValidator
from django.conf import settings



class Project(models.Model):

    hours_regex = RegexValidator(regex=r'^\d{0,5}$',
                                 message="Hours must be between 0 to 5 digits, includes 2 decimal.")
    
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    extimated_hours = models.DecimalField(max_digits=5, decimal_places=2, validators=[hours_regex], null=True, blank=True)
    actual_hours = models.DecimalField(max_digits=5, decimal_places=2, validators=[hours_regex], null=True, blank=True)
    is_ended = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"
