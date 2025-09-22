from django.db import models

class Article(models.Model):
    # 添加分类字段
    CATEGORY_CHOICES = (
        ('training', '训练'),
        ('rules', '规则'),
    )
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='training')

    def __str__(self):
        return self.title

class ArticleImage(models.Model):
    article = models.ForeignKey(Article, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="article_images/")

class ArticleVideo(models.Model):
    article = models.ForeignKey(Article, related_name="videos", on_delete=models.CASCADE)
    video = models.FileField(upload_to="article_videos/")