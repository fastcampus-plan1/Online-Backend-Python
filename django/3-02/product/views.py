from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.contrib.auth.decorators import permission_required
from .models import ProductOption


def login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponse("로그인 성공")
    else:
        return HttpResponse("로그인 실패")
    

def logout_view(request):
    logout(request)
    return HttpResponse("로그아웃 성공")


def view1(request):
    if request.user.is_authenticated:
        return HttpResponse("로그인 되어 있습니다.")
    else:
        return HttpResponse("로그인 되어 있지 않습니다.")


@login_required
def view2(request):
    return HttpResponse("로그인 되어 있습니다.")


class View3(LoginRequiredMixin, View):
    def get(self, request):
        return HttpResponse("로그인 되어 있습니다.")


def increase_sotck(request):
    if not request.user.has_perm("product.can_update_stock"):
        raise PermissionError("재고를 업데이트할 권한이 없습니다.")
    option = ProductOption.objects.get(pk=1)
    option.stock += 1
    option.save()
    return HttpResponse(f"재고를 추가 했습니다. 현재 재고: {option.stock}개")


# raise_exception=True로 설정하면, 권한이 없을 때 PermissionDenied 예외가 발생합니다.
# raise_exception=False로 설정하면 권한이 없을 때 로그인 페이지로 리다이렉트 됩니다.
@permission_required("product.can_update_stock", raise_exception=True)
def decrease_stock(request):
    option = ProductOption.objects.get(pk=1)
    option.stock -= 1
    if option.stock < 0:
        raise ValueError("재고가 부족합니다.")
    option.save()
    return HttpResponse(f"재고를 차감 했습니다. 현재 재고: {option.stock}개")
