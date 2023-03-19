from django.urls import include, path
from address.api.api_views import (
    AddressUserCreate,
    AddressUserUpdate,
    WardsDetail,
    WardsList,
    DistrictsDetail,
    DistrictsList,
    ProvincesDetail,
    ProvincesList,
    DeliveryAddressCreate,
    DeliveryAddressUpdate,
    DeliveryAddressList,
)

urlpatterns = [
    path('address-user/create', AddressUserCreate.as_view()),
    path('address-user/update/<int:id>', AddressUserUpdate.as_view()),
    path('delivery-address/create', DeliveryAddressCreate.as_view()),
    path('delivery-address/update/<int:id>', DeliveryAddressUpdate.as_view()),
    path('delivery-address/list', DeliveryAddressList.as_view()),
    path('wards/<str:code>/', WardsDetail.as_view()),
    path('wards-list/<str:district_code>', WardsList.as_view()),
    path('districts/<str:code>', DistrictsDetail.as_view()),
    path('districts-list/<str:province_code>', DistrictsList.as_view()),
    path('provinces/<str:code>', ProvincesDetail.as_view()),
    path('provinces-list', ProvincesList.as_view()),
]