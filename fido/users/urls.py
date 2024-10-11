from django.urls import path
from .views import UserDetailView, ManageFriendView, UserListView

urlpatterns = [
    path('api/v1/users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('api/v1/users/friends/', ManageFriendView.as_view(), name='manage-friends'),
    path('api/v1/users/all/', UserListView.as_view(), name='user-list'),
]
