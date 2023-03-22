from django.db import models


class Summary(models.Model):
    title = models.CharField(max_length=200)
    link = models.URLField(max_length=200)
    summaries = models.TextField()
    image_url = models.URLField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

class NewsArticle(models.Model):
    title = models.CharField(max_length=100)
    link = models.URLField()
    summary = models.TextField()
    image = models.URLField()

    def __str__(self):
        return self.title
