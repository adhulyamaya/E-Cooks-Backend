from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('login/',LoginView.as_view(),name="login"),
    path('google-login/', GoogleLoginView.as_view(), name='google-login'),
    path('signup/',SignupView.as_view(),name="signup"),
    # path('home/',HomeView.as_view(),name="home"),
    path('image-upload/',ImageuploadView.as_view(),name="image-upload"),
    path('create-data/',CreateView.as_view(),name="create"),
    path('geteditdata/<int:id>',GetEditView.as_view(),name="edit"),
    path('editing/',EditingView.as_view(),name="editing"),
    path('deleteuser/<int:id>',DeleteView.as_view(),name="deleteuser"),
    path('searchuser/',SearchView.as_view(),name="searchuser"),
    path('course-listing/',CourseListing.as_view(),name="courselisting"),
    path('purchased-courses/',PurchasedCourseListing.as_view(),name="purchased-courses")


]


