from django.db import models

class Task(models.Model):
    title = models.TextField(max_length=200)
    description = models.TextField(max_length=1000, null=True)

    def __str__(self):
        return self.title
    
    