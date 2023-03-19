# Generated by Django 4.1.7 on 2023-03-13 08:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('address', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('total_price', models.FloatField(default=0)),
                ('order_status', models.IntegerField(choices=[(0, 'hủy bỏ'), (1, 'đã xác nhận'), (2, 'chưa xác nhận'), (3, 'đang giao'), (4, 'đã giao')], default=2)),
                ('payment_status', models.IntegerField(choices=[(0, 'chưa thanh toán'), (1, 'đã thanh toán')], default=0)),
                ('payment_method', models.IntegerField(choices=[(0, 'cash'), (1, 'momo')], default=0)),
                ('delivery_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='delivery_address_order', to='address.deliveryaddress')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('price', models.FloatField(default=0)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orderitems_order', to='orders.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orderitems_product', to='products.product')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='carts_product', to='products.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='carts_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'product')},
            },
        ),
    ]