from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class patient(models.Model):
	p_userid = models.CharField(primary_key=True, max_length=20)
	p_name = models.CharField(max_length=200,blank=True)
	p_email=models.EmailField(max_length=254,blank=True)
	p_pass = models.CharField(max_length=254)
	p_ph = PhoneNumberField(blank=True)
	p_gender = models.CharField( max_length=20,blank=True)
	p_diabetic = models.CharField( max_length=20, blank=True)
