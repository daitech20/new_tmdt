<template>
    <a-layout v-if="isLoggedIn" style="min-height: 100vh">
		<DashBoardSlibar/>
		<a-layout>
			<DashBoardHeader/>
            <a-layout>
                <a-page-header
                style="border: 1px solid rgb(235, 237, 240)"
                title="Chi tiết đơn hàng"
                sub-title="" />
                    <a-layout-content style="padding: 0 50px">
                        <div class="info-address">
                            <h3>Tên người nhận: {{ order.delivery_address.recipient_first_name }} {{ order.delivery_address.recipient_last_name }}</h3>
                            <h3>Địa chỉ nhận hàng: {{ order.delivery_address.address }}</h3>
                            <h3>Số điện thoại: {{ order.delivery_address.phone }}</h3>
                            <h3>Trạng thái đơn hàng: 
                                <a v-if="order.order_status==0">Hủy đơn</a>
                                <a v-if="order.order_status==1">Đã xác nhận</a>
                                <a v-if="order.order_status==2">Chưa xác nhận</a>
                                <a v-if="order.order_status==3">Đang giao</a>
                                <a v-if="order.order_status==4">Đã giao</a>
                            </h3>
                            <h3>Phương thức thanh toán: 
                                <a v-if="order.payment_method==0">Tiền mặt</a>
                                <a v-if="order.payment_method==1">Momo</a>
                            </h3>
                            <h3>Thanh toán: 
                                <a v-if="order.payment_status==0">Chưa thanh toán</a>
                                <a v-if="order.payment_status==1">Đã thanh toán</a>
                            </h3>
                        </div>
                        <a-table class="ant-table-striped" :columns="columns" :data-source="data" :scroll="{ x: 1000, y: 500 }" >
                            <template #bodyCell="{ column, record }">
                                <template v-if="column.dataIndex === 'image'">
                                    <a-image
                                        :width="50"
                                        :src="record.image"
                                    />
                                </template>
                            </template>
                        </a-table>
                        <div class="cart-summary">
                            <h3>Tổng tiền đơn hàng: {{ order.total_price }} vnd</h3>
                        </div>
                    </a-layout-content>
            </a-layout>
            <DashBoardFooter/>
        </a-layout>
    </a-layout>
</template>

<script>

import { authStore } from '../../store/auth.store'
import { mapState } from 'pinia';
import BaseRequest from '../../core/BaseRequest.js';
import { notification } from 'ant-design-vue';
import DashBoardSlibar from '../../components/DashBoard/DashBoardSlibar.vue'
import DashBoardHeader from '../../components/DashBoard/DashBoardHeader.vue'
import DashBoardFooter from '../../components/DashBoard/DashBoardFooter.vue'


export default {
    data() {
        return {
            order: {
                delivery_address: {
                    phone: "",
                    recipient_last_name: "",
                    recipient_first_name: "",
                    address: ""
                },
                order_status: 1,
                payment_status: 0,
                payment_method: 0,
                total_price: 0
            },
			order_items: [],
            columns: [],
            data: [],
        }
    },
    components: {
        DashBoardSlibar, DashBoardHeader, DashBoardFooter
    },
	mounted() {
		this.getOrderItems()
	},
	computed: {
		...mapState(authStore, ['isLoggedIn', 'user'])
	},
    methods: {
		showModalLogin: function() {
			this.visible_login = true
		},
		handleLogin: function() {
			this.$router.push({ name: 'login'});
		},
        getOrderItems: function(){
            this.columns = [
                {
				title: 'Id',
				dataIndex: 'id',
				key: 'id'
				},
				{
				title: 'Tên sản phẩm',
				dataIndex: 'name',
				key: 'name'
				},
				{
				title: 'HÌnh ảnh',
				dataIndex: 'image',
				key: 'image'
				},
				{
				title: 'Giá',
				dataIndex: 'price',
				key: 'price'
				},
                {
				title: 'Số lượng',
				dataIndex: 'quantity',
				key: 'quantity'
				},
                {
				title: 'Lựa chọn',
				dataIndex: 'option',
				key: 'option'
				},
			];

			if (this.user) {
				BaseRequest.get('orders/order/detail/' + this.$route.params.order_id)
				.then(response => {
					this.order = response.data
                    this.order_items = this.order.orderitems_order
					for (const num in this.order_items) {
                        this.data.push({
                            name: this.order_items[num].product.name,
							image: this.order_items[num].product.image,
							price: this.order_items[num].product.price,
							quantity: this.order_items[num].quantity,
							id: this.order_items[num].id
						})
					}
				})
				.catch(error=> {
					this.errors = error.response.data
					console.log("error")
				});
			}
            else {
                this.handleLogin()
            }
        },
    }
}
</script>

<style scoped>
</style>