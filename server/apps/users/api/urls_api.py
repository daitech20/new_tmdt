from django.urls import include, path
from users.api.api_views import (
    RegisterCustomerView,
    MyTokenObtainPairView,
    RegisterStaffView,
    StaffUpdate,
    CustomerUpdate,
    UserDetail,
)
from rest_framework_simplejwt.views import TokenRefreshView



urlpatterns = [
    path('register/customer', RegisterCustomerView.as_view()),
    path('register/staff', RegisterStaffView.as_view()),
    path('user/<str:username>', UserDetail.as_view()),
    path('staff/update/<int:id>', StaffUpdate.as_view()),
    path('customer/update/<int:id>', CustomerUpdate.as_view()),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]