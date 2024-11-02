from django.db import models

# Create your models here.
class Note(models.Model):
    note = models.CharField(max_length=200, primary_key=True)

    def __str__(self): 
        return self.note