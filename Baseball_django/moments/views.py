from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.db.models import Q
from django.core.paginator import Paginator
import json

from .models import Moment, MomentLike, MomentComment, UserProfile, MomentImage
from .forms import MomentForm, UserProfileForm

def register_view(request):
    """用户注册"""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # 创建用户资料
            UserProfile.objects.create(user=user, nickname=user.username)
            messages.success(request, '注册成功！')
            return redirect('moments:login')
    else:
        form = UserCreationForm()
    return render(request, 'moments/register.html', {'form': form})

def login_view(request):
    """用户登录"""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, '登录成功！')
            return redirect('moments:moments_list')
        else:
            messages.error(request, '用户名或密码错误')
    return render(request, 'moments/login.html')

@login_required
def moments_list(request):
    """时刻列表"""
    moments = Moment.objects.filter(is_public=True).select_related('author').prefetch_related('likes', 'comments')
    
    # 搜索功能
    search_query = request.GET.get('search')
    if search_query:
        moments = moments.filter(
            Q(content__icontains=search_query) | 
            Q(author__username__icontains=search_query)
        )
    
    # 分页
    paginator = Paginator(moments, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'search_query': search_query,
    }
    return render(request, 'moments/moments_list.html', context)

@login_required
def create_moment(request):
    """创建时刻"""
    if request.method == 'POST':
        form = MomentForm(request.POST, request.FILES)
        if form.is_valid():
            moment = form.save(commit=False)
            moment.author = request.user
            moment.save()
            
            # 处理多张图片上传
            images = form.cleaned_data.get('images', [])
            if not isinstance(images, list):
                images = [images] if images else []
            
            for image in images:
                if image:  # 确保图片不为空
                    MomentImage.objects.create(moment=moment, image=image)
            
            messages.success(request, '时刻发布成功！')
            return redirect('moments:moments_list')
    else:
        form = MomentForm()
    return render(request, 'moments/create_moment.html', {'form': form})

@login_required
def moment_detail(request, moment_id):
    """时刻详情"""
    moment = get_object_or_404(Moment, id=moment_id, is_public=True)
    comments = moment.comments.all().order_by('created_at')
    
    context = {
        'moment': moment,
        'comments': comments,
    }
    return render(request, 'moments/moment_detail.html', context)

@login_required
@require_POST
@csrf_exempt
def like_moment(request, moment_id):
    """点赞/取消点赞时刻"""
    moment = get_object_or_404(Moment, id=moment_id)
    like, created = MomentLike.objects.get_or_create(
        user=request.user,
        moment=moment
    )
    
    if not created:
        like.delete()
        moment.likes_count -= 1
        liked = False
    else:
        moment.likes_count += 1
        liked = True
    
    moment.save()
    
    return JsonResponse({
        'liked': liked,
        'likes_count': moment.likes_count
    })

@login_required
@require_POST
def add_comment(request, moment_id):
    """添加评论"""
    moment = get_object_or_404(Moment, id=moment_id)
    content = request.POST.get('content', '').strip()
    
    if content:
        MomentComment.objects.create(
            user=request.user,
            moment=moment,
            content=content
        )
        moment.comments_count += 1
        moment.save()
        messages.success(request, '评论添加成功！')
    else:
        messages.error(request, '评论内容不能为空')
    
    return redirect('moments:moment_detail', moment_id=moment_id)

@login_required
def profile_view(request):
    """用户资料页面"""
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    user_moments = Moment.objects.filter(author=request.user).order_by('-created_at')
    
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, '资料更新成功！')
            return redirect('moments:profile')
    else:
        form = UserProfileForm(instance=profile)
    
    context = {
        'profile': profile,
        'form': form,
        'user_moments': user_moments,
    }
    return render(request, 'moments/profile.html', context)