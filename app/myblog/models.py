from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
# Create your models here.
# add blog categories here
blog_cat = (
        ('TECHNOLOGY','tech'),
        ('PYTHON','py'),
        ('JAVA SCRIPT','js'),
        ('JAVA','java'),
    )
# Model for creating new blog posts
class post(models.Model):
    srl= models.AutoField(primary_key=True)
    title= models.CharField(max_length=500)
    desc= models.TextField(default='')
    content= models.TextField()
    author= models.ForeignKey('author', on_delete= models.RESTRICT)
    clickRate= models.IntegerField(default=0)
    category= models.ForeignKey('category', on_delete= models.CASCADE)
    slug= models.SlugField(max_length=200,unique=True)
    time= models.DateTimeField(blank=True)
    image= models.ImageField(default='default_image_post.jpg')
    def __str__(self):
        return f"{self.title} (written by {self.author})"
# Model for creating new category
class category(models.Model):
    srl= models.AutoField(primary_key=True)
    name= models.CharField(max_length=50, blank=True, choices=blog_cat)
    desc= models.TextField()
    image= models.ImageField(default='default_image_cat.jpg')
    time= models.TimeField(auto_now=True)
    def __str__(self):
        return self.name
#  Model for creating new author profile
class author(models.Model):
    name= models.CharField(max_length=50, blank=True)
    about= models.CharField(max_length=500)
    designation= models.CharField(max_length=100, default='')
    image= models.ImageField(default='default_image_auth.jpg')
    def __str__(self):
        return self.name
# Model for comment
class BlogComment(models.Model):
    sno= models.AutoField(primary_key=True)
    comment= models.TextField()
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    post= models.ForeignKey(post, on_delete=models.CASCADE)
    parent= models.ForeignKey("self", on_delete=models.CASCADE, null=True)
    time= models.DateTimeField(default=now)
    def __str__(self):
        return f"comment by {self.user} on {self.post}"