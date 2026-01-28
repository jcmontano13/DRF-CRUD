from django.db import models

# created database table named Activity (inherit from models.Model)
class Activity(models.Model):
    type = models.CharField(max_length=100)
    date_time = models.DateTimeField()
    duration = models.IntegerField()
    status = models.CharField(max_length=50)
    remarks = models.TextField(blank=True)

    def __str__(self):
        return f"{self.type} - {self.status}"