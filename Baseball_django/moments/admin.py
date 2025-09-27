from django.contrib import admin
from .models import UserProfile, Moment, MomentLike, MomentComment

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'nickname', 'created_at']
    list_filter = ['created_at']
    search_fields = ['user__username', 'nickname']
    readonly_fields = ['created_at']

@admin.register(Moment)
class MomentAdmin(admin.ModelAdmin):
    list_display = ['author', 'content_preview', 'likes_count', 'comments_count', 'created_at', 'is_public']
    list_filter = ['is_public', 'created_at']
    search_fields = ['content', 'author__username']
    readonly_fields = ['likes_count', 'comments_count', 'created_at', 'updated_at']
    
    def content_preview(self, obj):
        return obj.content[:50] + '...' if len(obj.content) > 50 else obj.content
    content_preview.short_description = '内容预览'

@admin.register(MomentLike)
class MomentLikeAdmin(admin.ModelAdmin):
    list_display = ['user', 'moment', 'created_at']
    list_filter = ['created_at']
    search_fields = ['user__username', 'moment__content']

@admin.register(MomentComment)
class MomentCommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'moment', 'content_preview', 'created_at']
    list_filter = ['created_at']
    search_fields = ['content', 'user__username', 'moment__content']
    
    def content_preview(self, obj):
        return obj.content[:30] + '...' if len(obj.content) > 30 else obj.content
    content_preview.short_description = '评论预览'