from django.db import models
from django.contrib.auth.models import User

class Complaint(models.Model):
    cid = models.AutoField(primary_key=True)
    complaint_text = models.TextField()
    email = models.EmailField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    file = models.FileField(upload_to='./img', blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    mobile_number = models.CharField(max_length=15, blank=True, null=True)
    viewed=models.BooleanField(default=False)
    complaintTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Complaint ID "+str(self.cid)
    

class Alerts(models.Model):
    aid = models.AutoField(primary_key=True)
    alertText = models.TextField()
    alertby=models.TextField()
    lat = models.FloatField(blank=True, null=True)
    lon = models.FloatField(blank=True, null=True)
    viewed=models.BooleanField(default=False)
    atime= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Alert ID "+str(self.aid)


