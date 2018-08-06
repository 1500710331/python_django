from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    """The topic of user learning"""
    text = models.CharField(max_length=200) 
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
    	"""return model's string"""
    	return self.text

    	
class Entry(models.Model):
	"""what you learn knowlege"""
	topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
	text = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)
	
	class Meta:
		verbose_name_plural = 'entries'

	def __str__(self):
		return self.text[:50] + "..."
