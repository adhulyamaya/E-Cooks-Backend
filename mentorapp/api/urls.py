from django.urls import path
from .views import *

urlpatterns = [
    path('mentorsignup/', MentorSignupView.as_view(), name='mentor_signup'),   
    path('mentorlogin/', MentorLoginView.as_view(), name='mentorlogin'), 
    path('mentoronboard/', MentorOnboard.as_view(), name='mentoronboard'), 
    path('addclass/',CreateclassView.as_view(),name='addclass'),
    path('editclass/',EditingClassView.as_view(),name='editclass'),
    path('geteditdata/<int:id>',GetEditView.as_view(),name="edit"),    
    path('deleteclass/<int:id>',DeleteView.as_view(),name="deleteclass"),
    path('classdetails/<int:id>/', ToggleEnableDisableView.as_view(), name='toggle_enable_disable'),
    path('classdetails/',ClassdetailsView.as_view(),name='classdetails'),
    path('mentor-availability/<int:mentor_id>/',MentorAvailabilityView.as_view(),name='classdetails'),
    # path('booking/',BookingStoringView.as_view(),name='booking'),
    path('storeOrder/',StoreOrderView.as_view(),name='storeOrder'),
    path('booking/',UpdateBookingDetailsView.as_view(),name='booking'),
    path('entrolledstudents/',EntrolledStudentsView.as_view(),name='entrolledstudents'),
     path('confirm-booking/<int:order_id>/', ConfirmBookingView.as_view(), name='confirm-booking'),
   

]
