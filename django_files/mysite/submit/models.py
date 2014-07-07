from django.db import models

# Create your models here.


class Job(models.Model):
	job_id = models.CharField(max_length=100)
	pub_date = models.DateTimeField('date submitted')
