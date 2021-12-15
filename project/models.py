from django.db import models

class Project(models.Model):
   id = models.AutoField(primary_key=True)
   created_by_user = models.TextField()
   created_by_user_email = models.EmailField()
   created_by_user_id = models.IntegerField()
   timestamp_initialCreation = models.DateField(auto_now=True)
   timestamp_lastUpdated = models.DateField(auto_now=True)
   title = models.TextField()
   description = models.TextField()



