from django.db import models

'''
django modle field:
-html widget
-validation
-db size

'''
# Create your models here.

JOB_TYPE=(
    ('Full Time','Full Time'),
    ('Part Time','Part Time'),
)
class Job(models.Model):    #table
    title=models.CharField(max_length=100)    #column
    #location
    job_type=models.CharField(max_length=15,choices=JOB_TYPE)
    description=models.TextField(max_length=1000)   
    published_at=models.DateTimeField(auto_now=True)
    vacancy=models.IntegerField(default=1)
    #category
    salary=models.IntegerField(default=0)
    experience=models.IntegerField(default=1)
    
    def __str__(self):
        return self.title