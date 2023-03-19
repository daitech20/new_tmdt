<template>
	
    <HomeHeader ref="Cart"/>
    <!-- BREADCRUMB -->
    <div id="breadcrumb" class="section">
        <!-- container -->
        <div class="container">
            <!-- row -->
            <div class="row">
                <div class="col-md-12">
                    <h3 class="breadcrumb-header">Tìm kiếm</h3>
                <ul class="breadcrumb-tree">
                    <li>
                        <router-link :to="{name: 'home'}">Home</router-link>
                    </li>
                    <li class="active">Tìm kiếm</li>
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
					<!-- STORE -->
					<div id="store" class="col-md-9">
                		<!-- store products -->
						<div class="row">
							<!-- product -->
                            <div class="products-slick">
                            <div v-for="product in products.slice(0,4)" class="product">
                                <div class="product-img">
                                    <img :src="product.image" alt="">
                                </div>
                                <div class="product-body">
                                    <p class="product-category">{{ product.category.name }}</p>
                                    <router-link :to="{name: 'product.home.detail', params: {product_id: product.id}}">
										<h3 class="product-name"><a href="#">{{ product.name }}</a></h3>
									</router-link>
                                    <h4 class="product-price">$ {{ product.price }} VND</h4>
                                </div>
                                <div class="add-to-cart">
                                    <button class="add-to-cart-btn"  @click="addToCart(product.id)"><i class="fa fa-shopping-cart"></i> add to cart</button>
                                </div>
                            </div>
                            <!-- /product -->
                            </div>
						</div>
						<!-- /store products -->
					</div>
					<!-- /STORE -->
				</div>
				<!-- /row -->
			</div>
			<!-- /container -->
		</div>
		<!-- /SECTION -->
        <a-modal v-model:visible="visible_login" title="Ban chua dang nhap">
			<template #footer>
				<a-button key="login" type="primary" @click="handleLogin()">Dang nhap</a-button>
			</template>
		</a-modal>
    <HomeFooter/>

</template>

<script>

import authService from '../../services/auth.service'
import { authStore } from '../../store/auth.store'
import { mapActions, mapState } from 'pinia';
import HomeHeader from '../../components/Home/HomeHeader.vue'
import HomeFooter from '../../components/Home/HomeFooter.vue'
import BaseRequest from '../../core/BaseRequest.js';
import { notification } from 'ant-design-vue';

export default {
    data() {
        return {
			products: [],
			visible_login: false,
        }
    },
	components: {
        HomeHeader,
        HomeFooter
    },
	mounted() {
		this.getProducts()
	},
	computed: {
		...mapState(authStore, ['isLoggedIn', 'user'])
	},
    methods: {
		getProducts: function() {
			this.data = []
			BaseRequest.get('products/product/list?search=' + this.$route.params.data_search)
			.then(response => {
				this.products = response.data
                console.log(this.products)
			})
			.catch(error=> {
				this.errors = error.response
				console.log(this.errors)
			});
		},

		showModalLogin: function() {
			this.visible_login = true
		},

		handleLogin: function() {
			this.$router.push({ name: 'login'});
		},

		addToCart: function(product_id) {
			if (this.isLoggedIn) {
				BaseRequest.post('orders/cart/create', {
					'product': product_id,
					'quantity': 1
				})
				.then(response => {
					console.log(response.data)
					this.$refs.Cart.getCarts()
					this.createSuccessNotification('Thành công', 'Thêm sản phẩm thành công')
				})
				.catch(error=> {
					this.errors = error.response
					console.log(this.errors)
				});
			}
			else {
				this.showModalLogin()
			}
		},

		createSuccessNotification: function(message, description) {
            notification['success']({
                message: message,
                description: description,
            });
        },
    }
}

</script>

<style scoped>
	
</style>