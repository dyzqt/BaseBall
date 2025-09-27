from django import forms
from .models import Moment, UserProfile

class MomentForm(forms.ModelForm):
    """时刻表单"""
    content = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 4,
            'placeholder': '分享你的想法和建议...'
        }),
        max_length=1000,
        label='内容'
    )
    
    image = forms.ImageField(
        required=False,
        widget=forms.FileInput(attrs={
            'class': 'form-control',
            'accept': 'image/*'
        }),
        label='图片'
    )
    
    class Meta:
        model = Moment
        fields = ['content', 'image']

class UserProfileForm(forms.ModelForm):
    """用户资料表单"""
    nickname = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '请输入昵称'
        }),
        label='昵称'
    )
    
    bio = forms.CharField(
        max_length=500,
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 3,
            'placeholder': '介绍一下自己...'
        }),
        label='个人简介'
    )
    
    avatar = forms.ImageField(
        required=False,
        widget=forms.FileInput(attrs={
            'class': 'form-control',
            'accept': 'image/*'
        }),
        label='头像'
    )
    
    class Meta:
        model = UserProfile
        fields = ['nickname', 'bio', 'avatar']
