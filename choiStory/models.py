from django.db import models

# Create your models here.
class blog(models.Model):

	title = models.CharField(max_length=50)
	preview = models.TextField(max_length=50)
	content = models.TextField(max_length=1000)
	posted = models.DateTimeField(auto_now_add=True)

	def __str__(self):
	    return self.title

