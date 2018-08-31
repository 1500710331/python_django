from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
	text = models.TextField(max_length=200)
	date_added = models.DateTimeField(auto_now_add=True)
	owner = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)

	def __str__(self):
		return self.text

class  Entry(models.Model):
	text = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)
	topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
	class Meta:
		verbose_name_plural = 'entries'


	def __str__(self):
		return self.text[:50] + "..."


class Img(models.Model):
    date_added = models.DateTimeField(auto_now_add=True)
    img_url = models.ImageField(upload_to='img', blank=False, null=False) # upload_to指定图片上传的途径，如果不存在则自动创建
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    
    class Meta:
    	db_table = 'photos'