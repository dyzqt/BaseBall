from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class UserProfile(models.Model):
    """用户扩展信息"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    nickname = models.CharField(max_length=50, blank=True, verbose_name='昵称')
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True, verbose_name='头像')
    bio = models.TextField(max_length=500, blank=True, verbose_name='个人简介')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    
    def __str__(self):
        return f"{self.user.username} - {self.nickname or '未设置昵称'}"
    
    class Meta:
        verbose_name = '用户资料'
        verbose_name_plural = '用户资料'

class Moment(models.Model):
    """我的时刻 - 用户分享的想法和建议"""
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='moments', verbose_name='作者')
    content = models.TextField(max_length=1000, verbose_name='内容')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    likes_count = models.PositiveIntegerField(default=0, verbose_name='点赞数')
    comments_count = models.PositiveIntegerField(default=0, verbose_name='评论数')
    is_public = models.BooleanField(default=True, verbose_name='是否公开')

class MomentImage(models.Model):
    """时刻图片"""
    moment = models.ForeignKey(Moment, on_delete=models.CASCADE, related_name='images', verbose_name='时刻')
    image = models.ImageField(upload_to='moment_images/', verbose_name='图片')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    
    class Meta:
        verbose_name = '时刻图片'
        verbose_name_plural = '时刻图片'
    
    def __str__(self):
        return f"{self.author.username} - {self.content[:50]}..."
    
    class Meta:
        verbose_name = '我的时刻'
        verbose_name_plural = '我的时刻'
        ordering = ['-created_at']

class MomentLike(models.Model):
    """时刻点赞"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户')
    moment = models.ForeignKey(Moment, on_delete=models.CASCADE, related_name='likes', verbose_name='时刻')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='点赞时间')
    
    class Meta:
        unique_together = ('user', 'moment')  # 防止重复点赞
        verbose_name = '时刻点赞'
        verbose_name_plural = '时刻点赞'

class MomentComment(models.Model):
    """时刻评论"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户')
    moment = models.ForeignKey(Moment, on_delete=models.CASCADE, related_name='comments', verbose_name='时刻')
    content = models.TextField(max_length=500, verbose_name='评论内容')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='评论时间')
    
    def __str__(self):
        return f"{self.user.username} - {self.content[:30]}..."
    
    class Meta:
        verbose_name = '时刻评论'
        verbose_name_plural = '时刻评论'
        ordering = ['created_at']