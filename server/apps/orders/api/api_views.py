from rest_framework import permissions
from core.permissions import IsOwnerOrReadOnly, IsStaffUser, IsSuperUser
from rest_framework import generics, status
from orders.api.serializers import (
    CartSerializer,
    CartListSerializer,
    OrderCreateSerializer,
    OrderListSerializer,
    OrderUpdateSerializer,
    OrderItemListSerializer
)
from orders.models import Cart, Order, OrderItem



class CartList(generics.ListAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartListSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        user = self.request.user

        return Cart.objects.filter(user=user).order_by('-id')


class CartUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart
    serializer_class = CartSerializer
    lookup_field = 'id'
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]


class CartCreate(generics.CreateAPIView):
    queryset = Cart
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class OrderCreate(generics.CreateAPIView):
    queryset = Order
    serializer_class = OrderCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class OrderList(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderListSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser or user.is_staff:
            return Order.objects.all()

        return Order.objects.filter(user=user).order_by('-id')


class OrderUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order
    serializer_class = OrderUpdateSerializer
    lookup_field = 'id'
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]


class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order
    serializer_class = OrderListSerializer
    lookup_field = 'id'
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]


class OrderItemList(generics.ListAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemListSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser or user.is_staff:
            return OrderItem.objects.all()

        return OrderItem.objects.filter(user=user).order_by('-id')