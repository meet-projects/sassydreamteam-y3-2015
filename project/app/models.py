from django.db import models



class Account(models.Model):
    firstnamesignup = models.CharField(max_length=12)
    lastnamesignup = models.CharField(max_length=16)
    usernamesignup = models.CharField(max_length=14)
    passwordsignup = models.CharField(max_length=18)
    emailsignup = models.EmailField()
 
