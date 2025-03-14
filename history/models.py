from django.db import models


class History(models.Model):
    equation = models.TextField()
            
    def __str__(self):
        return self.equation
    
    class Meta:
        db_table = 'History'



