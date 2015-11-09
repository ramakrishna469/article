from django.db import models

class Article(models.Model):
	name = models.CharField(max_length=200)
	author = models.CharField(max_length=200)
	description = models.TextField()
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name
