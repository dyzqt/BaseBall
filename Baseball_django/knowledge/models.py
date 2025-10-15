from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200)         # 标题
    content = models.TextField()                     # 内容
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=100, default='training')  # 添加category字段

    def __str__(self):
        return self.title

class ArticleImage(models.Model):
    article = models.ForeignKey(Article, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='article_images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class ArticleVideo(models.Model):
    article = models.ForeignKey(Article, related_name='videos', on_delete=models.CASCADE)
    video = models.FileField(upload_to='article_videos/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

# Create your models here.