from django.urls import path

from apps.users.views import (UserRetrieveUpdateDestroyView,
                              UsersAddAutoParkView, UsersListCreateView)

urlpatterns = [
    path('', UsersListCreateView.as_view(), name='user_list_create'),
    path('/<int:pk>', UserRetrieveUpdateDestroyView.as_view(), name='user_list_retrieve_update_delete'),
    path('/<int:pk>/auto_parks', UsersAddAutoParkView.as_view(), name='users_add_auto_park'),
]