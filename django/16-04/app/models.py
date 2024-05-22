from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=200, verbose_name='제목')
    content = models.TextField
    published_date = models.DateTimeField(auto_now_add=True, verbose_name='게시 날짜')
    author = models.CharField(max_length=100, verbose_name='작성자')
    read_count = models.IntegerField(default=1, verbose_name='조회수')

    class Meta:
        verbose_name = '블로그 포스트'
        verbose_name_plural = '블로그 포스트'