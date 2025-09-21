from django.shortcuts import render
from django.http import JsonResponse
from .models import Article

# 新增：主页视图（对应 urls.py 中的 home 导入）
def home(request):
    return render(request, "home.html")  # 渲染主页模板

# 文章列表视图（保持不变，确保 urls.py 中 article_list 导入有效）
def article_list(request):
    # 确保查询包含所有需要显示的字段
    articles = Article.objects.all().values("id", "title", "content", "created_at")
    return JsonResponse(list(articles), safe=False)
