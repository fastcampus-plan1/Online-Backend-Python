from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render

@staff_member_required
def index(request):
    title = "통계"
    data = [10000, 12000, 11000, 8000, 20000, 24000, 28000]
    return render(request, "statistics/index.html", {
        "title": title, 
        "has_permission": True,
        "data": data,
    })
