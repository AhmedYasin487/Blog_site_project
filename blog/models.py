from django.db import models
from django.urls import reverse
from django.utils import timezone

class Post(models.Model):

    author = models.ForeignKey("auth.User", verbose_name=("Author"), on_delete=models.CASCADE) #Diffterent
    title = models.CharField(("Title"), max_length=200)
    text = models.TextField("Text")
    created_date = models.DateTimeField(default = timezone.now) #Different
    published_date = models.DateTimeField(blank = True ,null = True)
  
    def publish(self):
        self.published_data = timezone.now()
        self.save()
    
    def approve_comment(self):
        return self.comments.filter(approved_comment = True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})

class Comment(models.Model):

    
    post = models.ForeignKey("blog.Post", related_name='comments', on_delete=models.CASCADE) #Views.py work make sense of this line later on
    author = models.CharField(("Author"), max_length=50)
    text = models.TextField(("Text"))
    created_date = models.DateTimeField(default =timezone.now) #Different
    approved_comment = models.BooleanField(default =False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse("post_list", kwargs={"pk": self.pk})

# Create your models here.
