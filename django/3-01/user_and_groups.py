from django.contrib.auth.models import User, Group, Permission

# group1 생성하고 Product 모든 권한 추가
group, created = Group.objects.get_or_create(name="group1")
product_permissions = Permission.objects.filter(content_type__app_label="product")
group.permissions.set(product_permissions)

# user2 생성하고 group1에 추가
try:
    user2 = User.objects.get(username="user2")
except User.DoesNotExist:
    user2 = User.objects.create_user(
        username="user2", 
        password="user1password", 
        email="user1@example.com",
    )
user2.groups.add(group)

# group1에 속한 사용자 확인
print("group1에 속한 사용자 확인:")
print(group.user_set.all())

# user2의 group1에 추가된 권한 확인
print("product.add_product 권한 확인:")
print(user2.has_perm("product.add_product"))
print("product.change_product 권한 확인:")
print(user2.has_perm("product.change_product"))
print("product.delete_product 권한 확인:")
print(user2.has_perm("product.delete_product"))
