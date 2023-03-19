<template>
    <link type="text/css" rel="stylesheet" href="css/bootstrap.min.css"/>
	<link rel="stylesheet" href="css/font-awesome.min.css">
	<link type="text/css" rel="stylesheet" href="css/style.css"/>
    <!-- /HEADER -->
    <HomeHeader ref="Cart"/>
    
	<!-- BREADCRUMB -->
    <div id="breadcrumb" class="section">
        <!-- container -->
        <div class="container">
            <!-- row -->
            <div class="row">
                <div class="col-md-12">
                    <h3 class="breadcrumb-header">Thanh toán</h3>
                <ul class="breadcrumb-tree">
                    <li>
                        <router-link :to="{name: 'home'}">Home</router-link>
                    </li>
                    <li class="active">Thanh toán</li>
                </ul>
                </div>
            </div>
            <!-- /row -->
        </div>
        <!-- /container -->
    </div>
    <!-- /BREADCRUMB -->


    <!-- SECTION -->
    <div class="section">
        <!-- container -->
        <div class="container">
            <!-- row -->
            <div class="row">

                <div class="col-md-7">
                    <!-- Billing Details -->
                    <div class="billing-details">
                        <div class="section-title">
                            <h3 class="title">Địa chỉ nhận hàng</h3>
                        </div>
                        <div>
                            <button  @click="showModalAddNewAddress()">Thêm địa chỉ mới</button>
                        </div>
                        <a-radio-group v-model:value="value_address">
                            <a-radio v-for="ad in address" :style="radioStyle" :value="ad.id">
                                {{ ad.address }}
                                <div>
                                    <text>Tên người nhận: {{ ad.recipient_first_name }}  {{ ad.recipient_last_name }}  phone: {{ ad.phone }}</text>                                
                                </div>
                            </a-radio>                            
                        </a-radio-group>
                    </div>
                    <!-- /Billing Details -->
                </div>

                <!-- Order Details -->
                <div class="col-md-5 order-details">
                    <div class="section-title text-center">
                        <h3 class="title">Đơn hàng của bạn</h3>
                    </div>
                    <div class="order-summary">
                        <div class="order-col">
                            <div><strong>Sản phẩm</strong></div>
                            <div><strong>Tổng cộng</strong></div>
                        </div>
                        <div class="order-products">
                            <div v-for="cart in carts" class="order-col">
                                <div>{{ cart.quantity }}x {{ cart.product.name }}</div>
                                <div>{{ cart.quantity * cart.product.price }}  VND</div>
                            </div>
                        </div>
                        <div class="order-col">
                            <div>Shiping</div>
                            <div><strong>FREE</strong></div>
                        </div>
                        <div class="order-col">
                            <div><strong>TOTAL</strong></div>
                            <div><strong class="order-total">{{ subtotal }} VND</strong></div>
                        </div>
                    </div>
                    <a class="primary-btn order-submit" @click="handlOrder">Đặt hàng</a>
                </div>
                <!-- /Order Details -->
            </div>
        <!-- /row -->
        </div>
        <!-- /container -->
        </div>
        <a-modal v-model:visible="visible_add_address" title="Thêm địa chỉ nhận hàng mới" @ok="addNewAddress">
        <a-form
            :model="new_address"
            name="nest-messages"
            :label-col="{ span: 8 }"
            :wrapper-col="{ span: 16 }"
            @finish="addNewAddress()"
        >
            <a-form-item
                :name="['recipient_first_name']"
                label="Họ người nhận"
                :rules="[{ required: true, message: 'Vui lòng nhập họ người nhận' }]"
            >
                <a-input v-model:value="new_address.recipient_first_name" />
            </a-form-item>
            
            <a-form-item
                :name="['recipient_last_name']"
                label="Tên người nhận"
                :rules="[{ required: true, message: 'Vui lòng nhập tên người nhận' }]"
            >
                <a-input v-model:value="new_address.recipient_last_name" />
            </a-form-item>

            <a-form-item
                :name="['province']"
                label="Tỉnh/ Thành phố"
            >
                <a-select
                    v-model:value="value_province"
                    label-in-value
                    style="width: 200px"
                    :options="options_province"
                ></a-select>
            </a-form-item>

            <a-form-item
                :name="['district']"
                label="Quận/ Huyện"
            >
                <a-select
                    v-model:value="value_district"
                    label-in-value
                    style="width: 200px"
                    :options="options_district"
                ></a-select>
            </a-form-item>

            <a-form-item
                :name="['ward']"
                label="Phường/ Xã"
            >
                <a-select
                    v-model:value="value_ward"
                    label-in-value
                    style="width: 200px"
                    :options="options_ward"
                ></a-select>
            </a-form-item>

            <a-form-item
                :name="['specific']"
                label="Địa chỉ cụ thể (số nhà):"
                :rules="[{ required: true, message: 'Vui lòng nhập Địa chỉ cụ thể !' }]"
            >
                <a-input v-model:value="new_address.specific" />
            </a-form-item>

            <a-form-item
                :name="['phone']"
                label="Phone"
                :rules="[{ required: true, message: 'Vui lòng nhập số điện thoại!' }]"
            >
                <a-input v-model:value="new_address.phone" />
            </a-form-item>

        </a-form>
    </a-modal>
	<!-- /SECTION -->

    <HomeFooter/>

</template>

<script>

import { authStore } from '../../store/auth.store'
import { mapActions, mapState } from 'pinia';
import HomeHeader from '../../components/Home/HomeHeader.vue'
import HomeFooter from '../../components/Home/HomeFooter.vue'
import BaseRequest from '../../core/BaseRequest.js';
import { notification } from 'ant-design-vue';

export default {
    data() {
        return {
			carts: [],
			subtotal: 0,
            columns: [],
            data: [],
            radioStyle: {
                display: 'flex',
                height: '60px',
                lineHeight: '30px',
            },
            value_address: null,
            address: [],
            visible_add_address: false,
            provinces: {},
            districts: {},
            wards: {},
            options_province: [],
            options_district: [],
            options_ward: [],
            value_province: {},
            value_district: {},
            value_ward: {},
            new_address: {
                specific: '',
                phone: '',
                recipient_first_name: '',
                recipient_last_name: '',
            },
        }
    },
	components: {
        HomeHeader,
        HomeFooter
    },
    watch: {
        value_province: function() {
            BaseRequest.get('address/districts-list/'+this.value_province.value)
			.then(response => {
				this.districts = response.data
                this.options_district = []
                for (let dt in this.districts) {
                    this.options_district.push(
                        {
                            value: this.districts[dt].code,
                            label: this.districts[dt].full_name
                        }
                    )
                }
                this.value_district = this.options_district[0]
			})
			.catch(error=> {
				this.errors = error.response
                console.log(this.errors)
			});
        },
        value_district: function() {
            BaseRequest.get('address/wards-list/'+this.value_district.value)
			.then(response => {
				this.wards = response.data
                this.options_ward = []
                for (let w in this.wards) {
                    this.options_ward.push(
                        {
                            value: this.wards[w].code,
                            label: this.wards[w].full_name
                        }
                    )
                }
                this.value_ward = this.options_ward[0]
			})
			.catch(error=> {
				this.errors = error.response
                console.log(this.errors)
			});
        }
    }
    ,
	mounted() {
		this.getCarts()
        this.getDeliveryAddress()
        this.getProvinces()
	},
	computed: {
		...mapState(authStore, ['isLoggedIn', 'user'])
	},
    methods: {
        ...mapActions(authStore, ['setAccessToken', 'setUser', 'setRefreshToken']),
		showModalLogin: function() {
			this.visible_login = true
		},
		handleLogin: function() {
			this.$router.push({ name: 'login-register'});
		},
        getProvinces: function() {
            BaseRequest.get('address/provinces-list')
			.then(response => {
				this.provinces = response.data
                for (let pr in this.provinces) {
                    this.options_province.push(
                        {
                            value: this.provinces[pr].code,
                            label: this.provinces[pr].full_name
                        }
                    )
                }
                this.value_province = this.options_province[0]
			})
			.catch(error=> {
				this.errors = error.response
                console.log(this.errors)
			});
        }
        ,
        getCarts: function(){
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
				BaseRequest.get('orders/cart/list')
				.then(response => {
					this.carts = response.data
                    this.subtotal = 0
					for (const num in this.carts) {
						this.subtotal += this.carts[num].quantity * this.carts[num].product.price
                        this.data.push({
                            name: this.carts[num].product.name,
							image: this.carts[num].product.image,
							price: this.carts[num].product.price,
							quantity: this.carts[num].quantity,
							id: this.carts[num].id
						})
					}
				})
				.catch(error=> {
					this.errors = error.response.data
					console.log("error")
				});
			}
        },
        getDeliveryAddress: function() {
            BaseRequest.get('address/delivery-address/list')
            .then(response => {
                this.address = response.data
                if (this.address) {
                    this.value_address=this.address[0].id
                }
                else{
                    this.value_address = null
                }
            })
            .catch(error=> {
                this.errors = error.response
            });
        },
        showModalAddNewAddress: function() {
            this.visible_add_address = true
        },
        addNewAddress: function() {
            BaseRequest.post('address/delivery-address/create', {
                specific: this.new_address.specific,
                phone: this.new_address.phone,
                recipient_first_name: this.new_address.recipient_first_name,
                recipient_last_name: this.new_address.recipient_last_name,
                ward: this.value_ward.value,

            })
            .then(response => {
                this.visible_add_address = false
                this.getDeliveryAddress()
                this.createSuccessNotification('Thành công', 'Thêm địa chỉ thành công')
            })
        },
        handlOrder: function() {
            BaseRequest.post('orders/order/create', {
                delivery_address: this.value_address
            })
            .then(response => {
                this.$refs.Cart.getCarts()
                this.createSuccessNotification('Thành công', 'Bạn đã đặt hàng thành công!')
                this.$router.push({ name: 'home'})
            })
            .catch(error=> {
                this.errors = error.response.data
                console.log(this.errors)
                if (this.errors.delivery_address) {
                    this.errorsNotification('Lỗi', 'Chưa thêm địa chỉ nhận hàng')
                }
            });
        },
        createSuccessNotification: function(message, description) {
            notification['success']({
                message: message,
                description: description,
            });
        },

        errorsNotification: function(message, description) {
            notification['error']({
                message: message,
                description: description,
            });
        }
    }
}
</script>

<style scoped>
</style>