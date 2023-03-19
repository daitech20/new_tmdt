from django.urls import include, path
from orders.api.api_views import (
    CartList,
    CartCreate,
    CartUpdate,
    OrderCreate,
    OrderList,
    OrderUpdate,
    OrderItemList,
    OrderDetail,
)


urlpatterns = [
    path('cart/list', CartList.as_view()),
    path('cart/create', CartCreate.as_view()),
    path('cart/update/<int:id>', CartUpdate.as_view()),
    path('order/create', OrderCreate.as_view()),
    path('order/list', OrderList.as_view()),
    path('order/detail/<int:id>', OrderDetail.as_view()),
    path('order/update/<int:id>', OrderUpdate.as_view()),
    path('order-item/list', OrderItemList.as_view()),
]