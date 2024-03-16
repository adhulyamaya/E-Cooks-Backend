from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('adminlogin/',AdminLoginView.as_view(),name="adminlogin"),
    path('admin-mentor-list/',MentorlistView.as_view(),name="admin-mentor-list"),
    path('admin-class-list/',ClasslistView.as_view(),name="admin-class-list"),
    path('mentor-approval/', MentorApprovalView.as_view(), name='mentor-approval'),
    path('toggle-block/<int:user_id>/', ToggleBlockUnblockView.as_view(), name='toggle_block'),
    path('admin-user-profile/',AdminprofileView.as_view(),name="admin-user-profile"),
    ]



