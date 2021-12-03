from django.db import models

class Genre(models.Model):
    genre_name = models.CharField(max_length=20)
    genre_id = models.AutoField(primary_key=True)

class Post(models.Model):
    title = models.CharField(max_length=20)
    review = models.CharField(max_length=1000)
    img_link = models.URLField()
    tags = models.CharField(max_length=20)
    date_created = models.DateTimeField()
    post_id = models.AutoField(primary_key=True)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    
class SocialTag(models.Model):
    name = models.CharField(max_length=20)
    socialtag_id = models.AutoField(primary_key=True)

class PostTag(models.Model):
    PostTag_id = models.AutoField(primary_key=True)
    socialtag_id = models.ForeignKey(SocialTag, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)