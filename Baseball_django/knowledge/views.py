from django.http import JsonResponse
from .models import Article
from django.db.models import Q
# 添加缺少的render导入
from django.shortcuts import render


# 主页视图
def home(request):
    return render(request, "home.html")


# 获取所有文章列表
def article_list(request):
    data = []
    for article in Article.objects.all().order_by("-created_at"):
        data.append({
            "id": article.id,
            "title": article.title,
            "content": article.content,
            "created_at": article.created_at.strftime("%Y-%m-%d"),
            "category": article.category,
            "images": [img.image.url for img in article.images.all()],
            "videos": [vid.video.url for vid in article.videos.all()],
        })
    return JsonResponse(data, safe=False)


# 按分类获取文章
def articles_by_category(request, category):
    # 转换中文分类名到英文
    category_map = {'训练': 'training', '规则': 'rules'}
    category_en = category_map.get(category, 'training')

    data = []
    for article in Article.objects.filter(category=category_en).order_by("-created_at"):
        data.append({
            "id": article.id,
            "title": article.title,
            "content": article.content,
            "created_at": article.created_at.strftime("%Y-%m-%d"),
            "category": article.category,
            "images": [img.image.url for img in article.images.all()],
            "videos": [vid.video.url for vid in article.videos.all()],
        })
    return JsonResponse(data, safe=False)


# 获取单个文章详情
def article_detail(request, article_id):
    try:
        article = Article.objects.get(id=article_id)
        data = {
            "id": article.id,
            "title": article.title,
            "content": article.content,
            "created_at": article.created_at.strftime("%Y-%m-%d"),
            "category": article.category,
            "images": [img.image.url for img in article.images.all()],
            "videos": [vid.video.url for vid in article.videos.all()],
        }
        return JsonResponse(data)
    except Article.DoesNotExist:
        return JsonResponse({"error": "Article not found"}, status=404)