from django.db import models
class Genre(models.Model):
    genre_name = models.CharField(max_length=20)
    genre_id = models.AutoField(primary_key=True)
class Tag(models.Model):
    name = models.CharField(max_length=100)
    socialtag_id = models.AutoField(primary_key=True)    
class Post(models.Model):
    title = models.CharField(max_length=20)
    review = models.CharField(max_length=1000)
    img_link = models.URLField()
    twitter = models.URLField(Tag,max_length=100)
    meta = models.URLField(Tag,max_length=100)
    instagram = models.URLField(Tag,max_length=100)
    linkedin = models.URLField(Tag,max_length=100)
    date_created = models.DateTimeField()
    post_id = models.AutoField(primary_key=True)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
