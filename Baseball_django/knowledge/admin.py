from django.contrib import admin
from .models import Article, ArticleImage, ArticleVideo

# 内联编辑图片
class ArticleImageInline(admin.TabularInline):
    model = ArticleImage
    extra = 1

# 内联编辑视频
class ArticleVideoInline(admin.TabularInline):
    model = ArticleVideo
    extra = 1

# 自定义Article的admin界面
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at')
    search_fields = ('title', 'content')
    list_filter = ('category', 'created_at')
    inlines = [ArticleImageInline, ArticleVideoInline]
    fields = ('title', 'category', 'content')

# 注册模型
admin.site.register(Article, ArticleAdmin)