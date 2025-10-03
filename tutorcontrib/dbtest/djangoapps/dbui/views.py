from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

User = get_user_model()

# @login_required
def users_page(request):
    users = User.objects.order_by("id").values("id", "username", "is_active")[:10]
    return render(request, "dbui/users.html", {"users": users})

# @login_required
def users_api(request):
    users = list(User.objects.order_by("id").values("id", "username", "is_active")[:10])
    return JsonResponse(users, safe=False)
