from django.db import models

from django.utils import timezone
from django.contrib.auth.models import User
from search import BlogPostIndex


# Create your models here.
class BlogPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blogpost')
    posted_date = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=255)
    text = models.TextField(max_length=1000)

    def __str__(self):
        return self.title

    def indexing(self):
        obj = BlogPostIndex(meta={
            'id': self.id,
            author = self.username,
            posted_date = self.posted_date,
            title = self.title,
            text = self.text
        })
        obj.save()
        return obj.to_dict(include_meta=True)