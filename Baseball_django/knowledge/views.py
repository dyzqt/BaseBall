from django.shortcuts import render
from django.http import JsonResponse
from .models import Article

# 新增：主页视图（对应 urls.py 中的 home 导入）
def home(request):
    return render(request, "home.html")  # 渲染主页模板

# 文章列表视图（保持不变，确保 urls.py 中 article_list 导入有效）
def serialize_article(article: Article):
    images = []
    if article.image:
        images.append(article.image.url)
    videos = []
    if article.video:
        videos.append(article.video.url)
    return {
        "id": article.id,
        "title": article.title,
        "content": article.content,
        "created_at": article.created_at.strftime("%Y-%m-%d %H:%M"),
        "category": article.category,
        "images": images,
        "videos": videos,
    }


def article_list(request):
    data = [serialize_article(a) for a in Article.objects.all().order_by("-created_at")]
    return JsonResponse(data, safe=False)


def articles_by_category(request, category: str):
    # 将前端的中文标签映射到存储值
    mapping = {"训练": "training", "规则": "rules"}
    stored = mapping.get(category, category)
    qs = Article.objects.filter(category=stored).order_by("-created_at")
    data = [serialize_article(a) for a in qs]
    return JsonResponse(data, safe=False)