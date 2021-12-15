from django.db import models

class Project(models.Model):
   id = models.AutoField(primary_key=True)
   created_by_user = models.TextField(default="Unknown")
   created_by_user_email = models.EmailField(default="none@nomail.com")
   created_by_user_id = models.IntegerField(default="1")
   timestamp_initialCreation = models.DateField(auto_now=True)
   timestamp_lastUpdated = models.DateField(auto_now=True)
   title = models.TextField(default="No text was entered")
   description = models.TextField(default="No text was entered")



