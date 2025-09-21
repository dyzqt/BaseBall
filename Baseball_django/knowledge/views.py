from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from .models import Article

#主页
def home(request):
    return render(request, 'home.html')  # 需确保模板文件存在
def article_list(request):
    articles = Article.objects.all().values("id", "title", "content", "created_at")
    # data = [
    #     {"id": 1, "title": "棒球规则基础", "content": "棒球是一项...", "created_at": "2025-09-21"},
    #     {"id": 2, "title": "投手与击球手", "content": "投手是...", "created_at": "2025-09-20"},
    # ]
    return JsonResponse(list(articles), safe=False)# safe=False 允许返回列表

