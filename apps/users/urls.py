from django.urls import include, path

from .views import UserCreateView, UserListView

urlpatterns = [
    path('', UserCreateView.as_view()),
    path('/list', UserListView.as_view())
]