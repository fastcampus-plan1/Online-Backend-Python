

from django.contrib.auth.models import User
# UserProfile 모델이 이미 정의되어 있다고 가정

# 특정 사용자 인스턴스를 가져옵니다.
user = User.objects.get(username='username')

# User 인스턴스에서 UserProfile로 역참조하여 접근
# OneToOneField를 사용했기 때문에, user 인스턴스를 통해 
# 직접 연결된 UserProfile에 접근할 수 있습니다.
user_profile = user.userprofile

# UserProfile의 바이오그래피 정보 출력
print(user_profile.bio)

