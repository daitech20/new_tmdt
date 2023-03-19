from django.db import models
from users.models import User
from products.models import Product
from address.models import DeliveryAddress
# Create your models here.
ORDER_STATUS = (
    (0, 'hủy bỏ'),
    (1, 'đã xác nhận'),
    (2, 'chưa xác nhận'),
    (3, 'đang giao'),
    (4, 'đã giao')
)

PAYMENT_METHODS = (
    (0, 'cash'),
    (1, 'momo')
)

PAYMENT_STATUS = (
    (0, 'chưa thanh toán'),
    (1, 'đã thanh toán')
)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="carts_user")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="carts_product")
    quantity = models.IntegerField(default=1)

    class Meta:
        unique_together = ('user', 'product',)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders_user")
    delivery_address = models.ForeignKey(DeliveryAddress, on_delete=models.CASCADE, related_name="delivery_address_order")
    created_at = models.DateTimeField(auto_now_add=True)
    total_price = models.FloatField(default=0)
    order_status = models.IntegerField(choices=ORDER_STATUS, default=2)
    payment_status = models.IntegerField(choices=PAYMENT_STATUS, default=0)
    payment_method = models.IntegerField(choices=PAYMENT_METHODS, default=0)

    def get_total_price(self):
        total = 0
        for order_item in self.orderitems_order.all():
            total += order_item.get_price()
        self.total_price = total
        return total
    
    def __str__(self) -> str:
        return self.user.username + str(self.created_at)


class OrderItem(models.Model):
    quantity = models.IntegerField(default=1)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="orderitems_product")
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="orderitems_order")
    price = models.FloatField(default=0)

    def get_price(self):
        self.price = self.product.price * self.quantity
        return self.product.price * self.quantity