from django.db import models

# Create your models here.

class Trustees(models.Model):
    team_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    designation = models.CharField(max_length=200,blank=True, null=True, default="Executive Member")
    about = models.CharField(max_length=400,blank=True,default="Dedicated member of SENA Foudation")
    # quote = models.CharField(max_length=40,blank=True,default="Dedicated member of SENA Foudation")
    # Social_media_handle = models.CharField(max_length=120)
    # handle_link = models.CharField(max_length=120)
    image  = models.ImageField(upload_to='team/',blank=True)
    def __str__(self):
        return self.name

class Leading_Team(models.Model):
    team_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    work = models.CharField(max_length=200,blank=True, null=True, default="Executive Member")
    area = models.CharField(max_length=20)
    about = models.CharField(max_length=400,blank=True,default="Dedicated member of SENA Foudation")
    # quote = models.CharField(max_length=40,blank=True,default="Dedicated member of SENA Foudation")
    # Social_media_handle = models.CharField(max_length=120)
    # handle_link = models.CharField(max_length=120)
    image  = models.ImageField(upload_to='team/',blank=True)
    def __str__(self):
        return self.name

class Advisory(models.Model):
    team_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    work = models.CharField(max_length=200,blank=True, null=True, default="Executive Member")
    about = models.CharField(max_length=400,blank=True,default="Dedicated member of SENA Foudation")
    # Social_media_handle = models.CharField(max_length=120)
    # handle_link = models.CharField(max_length=120)
    image  = models.ImageField(upload_to='team/',blank=True)
    def __str__(self):
        return self.name
