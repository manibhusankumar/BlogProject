from django.db import models

# Create your models here.

class blog(models.Model):
	title=models.CharField(max_length=70)
	content=models.CharField(max_length=100)
	date=models.DateTimeField()
	image=models.ImageField()

	def __str__(self):
		return self.title
		
