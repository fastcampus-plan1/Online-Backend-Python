from blog.models import Category, Post

# 새 카테고리 생성
category = Category.objects.create(name='프로그래밍')

# 새 포스트 생성 및 카테고리 연결
post = Post.objects.create(
    title='Django의 ForeignKey 이해하기', 
    content='...', 
    category=category,
)

# 포스트의 카테고리 이름 얻기
post_category_name = post.category.name

# 카테고리에 속한 포스트들에 접근
posts_in_category = category.posts.all()

print('포스트의 카테고리 이름:', post_category_name)
print('카테고리에 속한 포스트들:', posts_in_category)
