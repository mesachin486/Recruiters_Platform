
from django.db import models
from django.core.exceptions import ValidationError
        
DEGREE_CHOICES = (
    ('None', 'None'),
    ('Matriculate', 'Matriculate'),
    ('Intermediate','Intermediate'),
    ('Bachelors', 'Bachelors'),
    ('Masters', 'Masters'),
    ('Doctoral', 'Doctoral'),

)
GENDER_CHOICES = (
    ('None', 'None'),
    ('Male', 'Male'),
    ('Female','Female'),
    ('Not to disclose', 'Not to disclose'),
)


def phone_validator(value):
    if len(str(value)) != 10:
        raise ValidationError(
            "Enter Valid phone Number")

def aadhaar_validator(value):
    if len(str(value)) != 12:
        raise ValidationError(
            "Enter Valid Aadhaar Number")
        
  
        
    
class Candidate(models.Model):
    name = models.CharField(max_length=255)
    status= models.CharField(max_length=255, default='Applied')
    contact= models.IntegerField() 
    highest_degree= models.CharField(max_length=255, choices=DEGREE_CHOICES, default='None')
    address= models.CharField(max_length=255)
    aadhaar = models.IntegerField()
    father_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=255, choices=GENDER_CHOICES, default='None')
    email= models.EmailField()
    work_experience = models.TextField(null=True)
    resume = models.FileField( null=True)
    
    def __str__(self):
        return self.name 

