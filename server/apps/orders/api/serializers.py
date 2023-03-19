from rest_framework import serializers
from orders.models import Cart, Order, OrderItem
from products.api.serializers import ProductListSerializer
from address.api.serializers import DeliveryAddressListSerializer

class CartSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.user')
    
    class Meta:
        model = Cart
        fields = '__all__'

    def create(self, validated_data):
        user = self.context['request'].user
        if Cart.objects.filter(product=validated_data["product"], user=user).exists():
            cart = Cart.objects.filter(product=validated_data["product"], user=user)[0]
            cart.quantity += validated_data["quantity"]
            cart.save()
            return cart
        
        else:
            return Cart.objects.create(**validated_data)  


class OrderItemListSerializer(serializers.ModelSerializer):
    product = ProductListSerializer()

    class Meta:
        model = OrderItem
        fields = '__all__'


class CartListSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.user')
    product = ProductListSerializer()

    class Meta:
        model = Cart
        fields = '__all__'


class OrderListSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.user')
    delivery_address = DeliveryAddressListSerializer()
    orderitems_order = OrderItemListSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'user', 'delivery_address', 'created_at', 'total_price', 'order_status', 'payment_status', 'payment_method', 'orderitems_order']


class OrderUpdateSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.user')
    
    class Meta:
        model = Order
        fields = ['order_status', 'payment_status','user']


class OrderCreateSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.user')
    
    class Meta:
        model = Order
        fields = '__all__'

    def create(self, validated_data):
        order = Order.objects.create(**validated_data)
        total_price = 0
        for cart in Cart.objects.filter(user=order.user):
            OrderItem.objects.create(order=order, quantity=cart.quantity, product=cart.product, price=cart.product.price * cart.quantity)
            total_price += cart.product.price * cart.quantity
        Cart.objects.filter(user=order.user).delete()        
        order.total_price = total_price
        order.save()
        
        return order