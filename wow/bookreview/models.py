from django.db import models

# Create your models here.
class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    img_link = models.URLField()
    title =  models.CharField(max_length=255)
    body = models.TextField()
    date_created = models.DateTimeField()
    
# creat a genre variable that would later be refrenced in the view.py that can be passed in the paramiters