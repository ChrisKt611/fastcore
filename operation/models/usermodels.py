from django.db import models

class User(models.Model):
	
	username = models.CharField(max_length=50)
	password = models.CharField(max_length=50)

	class Meta:
		app_label = 'operation'
	
	def __unicode__(self):
		return self.username
