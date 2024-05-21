from book.models import Author, Book

# 저자 생성
author1 = Author.objects.create(name='김저자')
author2 = Author.objects.create(name='박작가')

# 책 생성
book1 = Book.objects.create(title='Django 마스터하기')
book2 = Book.objects.create(title='파이썬으로 시작하는 프로그래밍')

# 책에 저자 추가
book1.authors.add(author1, author2)
book2.authors.add(author1)

# 책 조회 시 저자 확인
for author in book1.authors.all():
    print(book1.title, '저자:', author.name)

# 저자 조회 시 쓴 책 확인 (역참조)
for book in author1.book_set.all():
    print(author1.name, '의 책:', book.title)
