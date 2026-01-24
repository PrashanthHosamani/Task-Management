from django.db import models

class Uncomplted_Task(models.Model):
    task = models.CharField(max_length=250)
    is_complted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.task
    
class Complted_Task(models.Model):
    pass
    
    