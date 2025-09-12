from django.urls import path
from .views import UserListCreateApiView, UserDetailApiview, RandomUserCreateApiView

urlpatterns = [
    path('user/', UserListCreateApiView.as_view(), name='user_list_create'),
    path('user/<int:pk>/', UserDetailApiview.as_view(), name='user_detail'),
    path('user/random/', RandomUserCreateApiView.as_view(), name='random_user'),
]
