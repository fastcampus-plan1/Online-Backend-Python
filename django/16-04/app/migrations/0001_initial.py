# Generated by Django 5.0.6 on 2024-05-22 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='제목')),
                ('published_date', models.DateTimeField(auto_now_add=True, verbose_name='게시 날짜')),
                ('author', models.CharField(max_length=100, verbose_name='작성자')),
            ],
            options={
                'verbose_name': '블로그 포스트',
                'verbose_name_plural': '블로그 포스트',
            },
        ),
    ]