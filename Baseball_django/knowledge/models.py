from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200)         # 标题
    content = models.TextField()                     # 内容
    created_at = models.DateTimeField(auto_now_add=True)
    # 分类（与现有迁移一致，默认 'training'）
    category = models.CharField(max_length=100, default='training')
    #图片
    image = models.ImageField(upload_to='article_images/', blank=True, null=True)
    # 添加视频字段
    video = models.FileField(upload_to='article_videos/', blank=True, null=True)
    def __str__(self):
        return self.title

# Create your models here.