from django import forms
from django.core.exceptions import ValidationError

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image', 'file']

    def clean_title(self):
        title = self.cleaned_data['title']
        if '[임시]' in title:
            raise ValidationError('제목에 [임시]를 포함할 수 없습니다.')
        return title
    
    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        content = cleaned_data.get('content')
        if title and content:
            if title == content:
                raise ValidationError('제목과 내용이 같습니다.')
        return cleaned_data