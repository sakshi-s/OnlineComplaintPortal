from django.db import models
from django.db import models
from django.contrib.auth.models import User

class Complaint(models.Model):
    place_choice = (
        ('Hostel', 'Hostel'),
        ('Campus', 'Campus')
    )
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.TextField()
    title = models.TextField()
    # image = models.FileField(null=True, )
    tag =models.CharField(choices=place_choice,max_length=25)



class Comment(models.Model):
    comp = models.ForeignKey(Complaint,on_delete = models.CASCADE)
    comment= models.CharField(max_length=250)