from django.urls import path, include
from knowledge.views import article_list, home, articles_by_category, article_detail
from django.conf import settings
from django.conf.urls.static import static
# 添加缺少的admin导入
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/', article_list),  # 获取所有文章列表
    path('articles/<str:category>/', articles_by_category),  # 按分类获取文章
    path('article/<int:article_id>/', article_detail),  # 获取单个文章详情
    path('moments/', include('moments.urls')),  # 我的时刻模块
    path('', home, name='home'),  # 主页
]
# 配置媒体文件和静态文件服务
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)