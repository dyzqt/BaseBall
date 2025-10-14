from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Article, ArticleImage, ArticleVideo

# 创建内联模型管理
class ArticleImageInline(admin.TabularInline):
    model = ArticleImage
    extra = 1  # 默认显示1个空的图片上传字段

class ArticleVideoInline(admin.TabularInline):
    model = ArticleVideo
    extra = 1  # 默认显示1个空的视频上传字段

# 修改文章管理以包含内联的图片和视频
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    inlines = [ArticleImageInline, ArticleVideoInline]