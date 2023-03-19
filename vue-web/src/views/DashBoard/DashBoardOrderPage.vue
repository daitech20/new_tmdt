<template>
	<a-layout v-if="isLoggedIn" style="min-height: 100vh">
		<DashBoardSlibar/>
		<a-layout>
			<DashBoardHeader/>
			<a-layout>
				<a-page-header
				style="border: 1px solid rgb(235, 237, 240)"
				title="Order"
				sub-title="Danh mục đơn hàng" />
				<a-layout-content style="padding: 0 50px">
					<a-table :columns="columns" :data-source="data" :scroll="{ x: 1000, y: 500 }">
						<template #bodyCell="{ column, record }">
                        <template v-if="column.dataIndex === 'id'">
							<router-link :to="{ name: 'order.detail', params: { order_id: record.id }}" >
								<a type="primary" size="small"> {{ record.id }} </a>
							</router-link>   
						</template>
						<template v-if="column.dataIndex === 'order_status'">
							<a v-if="record.order_status == 0" type="primary" size="small"> Hủy đơn </a>
                            <a v-if="record.order_status == 1" type="primary" size="small"> Đã xác nhận </a>
                            <a v-if="record.order_status == 2" type="primary" size="small"> Chưa xác nhận </a>
                            <a v-if="record.order_status == 3" type="primary" size="small"> Đang giao </a>
                            <a v-if="record.order_status == 4" type="primary" size="small"> Đã giao </a>
						</template>
                        <template v-if="column.dataIndex === 'payment_method'">
							<a v-if="record.payment_method == 0" type="primary" size="small"> Tiền mặt </a>
                            <a v-if="record.payment_method == 1" type="primary" size="small"> Momo </a>
						</template>
                        <template v-if="column.dataIndex === 'payment_status'">
							<a v-if="record.payment_status == 0" type="primary" size="small"> Chưa thanh toán </a>
                            <a v-if="record.payment_status == 1" type="primary" size="small"> Đã thanh toán </a>
						</template>
						<template v-if="column.dataIndex === 'option'">
							<a-button style="margin:2px" type="primary" danger size="small" @click="showModalDelete(record.id, record.name)">Hủy đơn</a-button>
							<a-button style="margin:2px" v-if="user.is_staff" type="primary" size="small" @click="showModalConfirm(record.id)">Xác nhận</a-button>
							<a-button style="margin:2px" v-if="user.is_staff" type="primary" size="small" @click="showModalShipping(record.id)">Đang ship</a-button>
							<a-button style="margin:2px" v-if="user.is_staff" type="primary" size="small" @click="showModalShipped(record.id)">Đã ship</a-button>
							<a-button style="margin:2px" v-if="user.is_staff" type="primary" size="small" @click="showModalPaid(record.id)">Đã thanh toán</a-button>
						</template>
						</template>
					</a-table>
				</a-layout-content>
				<a-modal v-model:visible="visible" title="Hủy đơn" @ok="handleDelete()">
				<p>
					Bạn muốn hủy đơn {{ this.order_name_del }}?
				</p>
				</a-modal>
				<a-modal v-model:visible="confirm_visible" title="Hủy đơn" @ok="handleConfirmOrder()">
				<p>
					Bạn muốn xác nhận đơn?
				</p>
				</a-modal>
				<a-modal v-model:visible="shipping_visible" title="Đang giao" @ok="handleShippingOrder()">
				<p>
					Đơn hàng đang ship
				</p>
				</a-modal>
				<a-modal v-model:visible="shipped_visible" title="Đã giao" @ok="handleShippedOrder()">
				<p>
					Đơn đã giao
				</p>
				</a-modal>
				<a-modal v-model:visible="paid_visible" title="Đã thanh toán" @ok="handlePaidOrder()">
				<p>
					Đã thanh toán
				</p>
				</a-modal>
			</a-layout>
			<DashBoardFooter/>
		</a-layout>
	</a-layout>
</template>

<script>

import BaseRequest from '../../core/BaseRequest.js';
import { authStore } from '../../store/auth.store';
import { mapState } from 'pinia';
import { notification } from 'ant-design-vue';
import DashBoardSlibar from '../../components/DashBoard/DashBoardSlibar.vue'
import DashBoardHeader from '../../components/DashBoard/DashBoardHeader.vue'
import DashBoardFooter from '../../components/DashBoard/DashBoardFooter.vue'

export default({
	data() {
		return {
			columns: [],
			orders: [],
			errors: {},
			data: [],
			visible: false,
            order_id_del: null,
            order_name_del: null,
			confirm_visible: false,
			order_id_confirm: null,
			shipping_visible: false,
			order_id_shipping: null,
			shipped_visible: false,
			order_id_shipped: null,
			paid_visible: false,
			order_id_paid: null
		}
	},
	mounted() {
		this.getData()
	},
	computed: {
		...mapState(authStore, ['isLoggedIn', 'user'])
	},
	components: {
        DashBoardSlibar, DashBoardHeader, DashBoardFooter
    },
	methods: {
		getData: function() {
			this.columns = [
                {
				title: 'Id',
				dataIndex: 'id',
				key: 'id'
				},
				{
				title: 'Địa chỉ',
				dataIndex: 'address',
				key: 'address'
				},
				{
				title: 'Ngày đặt',
				dataIndex: 'created_at',
				key: 'created_at'
				},
                {
				title: 'Tổng tiền',
				dataIndex: 'total_price',
				key: 'total_price'
				},
                {
				title: 'Trạng thái đơn hàng',
				dataIndex: 'order_status',
				key: 'order_status'
				},
                {
				title: 'Phương thức thanh toán',
				dataIndex: 'payment_method',
				key: 'payment_method'
				},
                {
				title: 'Đã thanh toán',
				dataIndex: 'payment_status',
				key: 'payment_status'
				},
                {
				title: 'Lựa chọn',
				dataIndex: 'option',
				key: 'option'
				},
			];

			this.getOrders()
		},
		getOrders: function() {
			this.data = []
			BaseRequest.get('orders/order/list')
			.then(response => {
				this.orders = response.data
				for (const num in this.orders) {
					this.data.push({
					    address: this.orders[num].delivery_address.address,
						created_at: this.orders[num].created_at,
                        id: this.orders[num].id,
                        total_price: this.orders[num].total_price,
                        order_status: this.orders[num].order_status,
						payment_method: this.orders[num].payment_method,
                        payment_status: this.orders[num].payment_status,
					})
				}
			})
			.catch(error=> {
				this.errors = error.response.data
			});
		},
        showModalDelete: function(id, name) {
			this.order_id_del = id
			this.order_name_del = name
			this.visible = true
		},
		showModalConfirm: function(id) {
			this.order_id_confirm = id
			this.confirm_visible = true
		},
		showModalShipping: function(id) {
			this.order_id_shipping = id
			this.shipping_visible = true
		},
		showModalShipped: function(id) {
			this.order_id_shipped = id
			this.shipped_visible = true
		},
		showModalPaid: function(id) {
			this.order_id_paid = id
			this.paid_visible = true
		},
        handleDelete: function() {
			this.visible = false
            BaseRequest.get('orders/order/update/' + this.order_id_del)
				.then(response => {
					let order_status = response.data.order_status
                    if (order_status == 2) {
                        BaseRequest.patch('orders/order/update/' + this.order_id_del, {
                            order_status: 0
                        })
                        .then(response => {
                            this.getOrders()
                            this.updateSuccessNotification()
                        })
                        .catch(error=> {
                            this.errors = error.response.data
                            console.log(this.errors)
                        });
                    }
                    else {
                        this.errorSuccessNotification('Thất bại', 'Đơn hàng đã xác nhận không thể hủy')
                    }
				})
				.catch(error=> {
					this.errors = error.response.data
				});
		},

		handleConfirmOrder: function() {
			this.confirm_visible = false
            BaseRequest.get('orders/order/update/' + this.order_id_confirm)
				.then(response => {
					let order_status = response.data.order_status
                    if (order_status == 0) {
                        this.errorSuccessNotification('Thất bại', 'Đơn hàng đã hủy')
                    }
                    else {
						BaseRequest.patch('orders/order/update/' + this.order_id_confirm, {
                            order_status: 1
                        })
                        .then(response => {
                            this.getOrders()
                            this.updateSuccessNotification()
                        })
                        .catch(error=> {
                            this.errors = error.response.data
                            console.log(this.errors)
                        });
					}
				})
				.catch(error=> {
					this.errors = error.response.data
				});
		},

		handleShippingOrder: function() {
			this.shipping_visible = false
            BaseRequest.get('orders/order/update/' + this.order_id_shipping)
				.then(response => {
					let order_status = response.data.order_status
                    if (order_status == 0) {
                        this.errorSuccessNotification('Thất bại', 'Đơn hàng đã hủy')
                    }
                    else {
						BaseRequest.patch('orders/order/update/' + this.order_id_shipping, {
                            order_status: 3
                        })
                        .then(response => {
                            this.getOrders()
                            this.updateSuccessNotification()
                        })
                        .catch(error=> {
                            this.errors = error.response.data
                            console.log(this.errors)
                        });
					}
				})
				.catch(error=> {
					this.errors = error.response.data
				});
		},
		handleShippedOrder: function() {
			this.shipped_visible = false
            BaseRequest.get('orders/order/update/' + this.order_id_shipped)
				.then(response => {
					let order_status = response.data.order_status
                    if (order_status == 0) {
                        this.errorSuccessNotification('Thất bại', 'Đơn hàng đã hủy')
                    }
                    else {
						BaseRequest.patch('orders/order/update/' + this.order_id_shipped, {
                            order_status: 4
                        })
                        .then(response => {
                            this.getOrders()
                            this.updateSuccessNotification()
                        })
                        .catch(error=> {
                            this.errors = error.response.data
                            console.log(this.errors)
                        });
					}
				})
				.catch(error=> {
					this.errors = error.response.data
				});
		},
		handlePaidOrder: function() {
			this.paid_visible = false
            BaseRequest.get('orders/order/update/' + this.order_id_paid)
				.then(response => {	
					BaseRequest.patch('orders/order/update/' + this.order_id_paid, {
						payment_status: 1
					})
					.then(response => {
						this.getOrders()
						this.updateSuccessNotification()
					})
					.catch(error=> {
						this.errors = error.response.data
						console.log(this.errors)
					});
						
					})
				.catch(error=> {
					this.errors = error.response.data
				});
		},
        updateSuccessNotification: function() {
			notification['success']({
				message: 'Update successfully!',
				description:
				'Order was update! ',
			});
		},
        errorSuccessNotification: function(message, descroption) {
			notification['error']({
				message: message,
				description: descroption,
			});
		}
	}
})
</script>