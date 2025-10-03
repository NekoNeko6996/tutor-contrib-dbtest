from django.urls import path
from . import views

app_name = "dbui"
urlpatterns = [
    path("dbtest/users", views.users_page, name="users_page"),
    path("api/dbtest/users", views.users_api, name="users_api"),
]
