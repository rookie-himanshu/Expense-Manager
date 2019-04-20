from django.db import models
from datetime import datetime

# Create your models here.
class expense(models.Model):
	title=models.CharField(max_length=500)
	description=models.TextField(blank=True,null=True)
	ammount=models.DecimalField(decimal_places=2,max_digits=10000)
	date=models.DateTimeField(default=datetime.now, blank=True)