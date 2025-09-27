from django.urls import path
from . import views

app_name = 'moments'

urlpatterns = [
    path('', views.moments_list, name='moments_list'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('create/', views.create_moment, name='create_moment'),
    path('moment/<int:moment_id>/', views.moment_detail, name='moment_detail'),
    path('moment/<int:moment_id>/like/', views.like_moment, name='like_moment'),
    path('moment/<int:moment_id>/comment/', views.add_comment, name='add_comment'),
    path('profile/', views.profile_view, name='profile'),
]
