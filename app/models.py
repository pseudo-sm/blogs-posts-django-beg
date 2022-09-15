from django.db import models

# Create your models here.
class Author(models.Model):

    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    is_active = models.BooleanField()
    gender = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

class Post(models.Model):

    title = models.CharField(max_length=255)
    content = models.TextField()
    create_date_time = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    image = models.FileField(upload_to="blog/app/media/posts",null=True,blank=True)

    def __str__(self):
        return self.title
    