<template>
    <header>
			<!-- TOP HEADER -->
			<div id="top-header">
				<div class="container">
					<ul class="header-links pull-right">
						<li v-if="user != null" >
							<a><i class="fa fa-user-o"></i> {{ user.username }} </a>

							<router-link :to="{ name: 'dashboard'}" >
								<a> DashBoard </a>
							</router-link>   

							<a @click="handleLogout"> Logout </a>
						</li>
						<li v-else>
							<router-link :to="{ name: 'login'}" >
								<a> Login</a>
							</router-link>   
						</li>
					</ul>
				</div>
			</div>
			<!-- /TOP HEADER -->

            <!-- MAIN HEADER -->
			<div id="header">
				<!-- container -->
				<div class="container">
					<!-- row -->
					<div class="row">
						<!-- LOGO -->
						<div class="col-md-3">
							<div class="header-logo">
								<a href="#" class="logo">
									<img src="../../../public/img/logo.png" alt="">
								</a>
							</div>
						</div>
						<!-- /LOGO -->

                        <!-- SEARCH BAR -->
						<div class="col-md-6">
							<div class="header-search">
								<form>
									
									<input v-model="data_search" class="input" placeholder="Search here">
									<button class="search-btn" @click="Search()">Search</button>
								</form>
							</div>
						</div>
						<!-- /SEARCH BAR -->

                        <!-- ACCOUNT -->
						<div class="col-md-3 clearfix">
							<div class="header-ctn">
                                <!-- Cart -->
								<div class="dropdown">
									<a class="dropdown-toggle" data-toggle="dropdown" aria-expanded="true">
										<i class="fa fa-shopping-cart"></i>
										<span>Your Cart</span>
										<div class="qty">{{ carts.length }}</div>
									</a>
									<div class="cart-dropdown">
										<div class="cart-list" v-if="this.user">
											<div v-for="cart in carts" class="product-widget">
												<div class="product-img">
													<img :src="cart.product.image" alt="">
												</div>
												<div class="product-body">
													<h3 class="product-name"><a href="#">{{ cart.product.name }}</a></h3>
													<h4 class="product-price"><span class="qty">{{ cart.quantity }}x</span>{{ cart.quantity * cart.product.price }} vnd</h4>
												</div>
												<button class="delete"><i class="fa fa-close"></i></button>
											</div>
										</div>
										<div class="cart-summary">
											<small>{{ carts.length }} Item(s) selected</small>
											<h5>SUBTOTAL: {{ subtotal }} vnd</h5>
										</div>
										<div class="cart-btns">
											<router-link :to="{name: 'cart.list'}">Xem giỏ</router-link>
											<router-link :to="{name: 'checkout'}">Đặt hàng</router-link>
											<i class="fa fa-arrow-circle-right"></i>
										</div>
									</div>
								</div>
								<!-- /Cart -->

                                <!-- Menu Toogle -->
								<div class="menu-toggle">
									<a href="#">
										<i class="fa fa-bars"></i>
										<span>Menu</span>
									</a>
								</div>
								<!-- /Menu Toogle -->
							</div>
						</div>
						<!-- /ACCOUNT -->
					</div>
					<!-- row -->
				</div>
				<!-- container -->
			</div>
			<!-- /MAIN HEADER -->
		</header>
		<!-- /HEADER -->

</template>

<script>
import { authStore } from '../../store/auth.store'
import { mapActions, mapState } from 'pinia';
import BaseRequest from '../../core/BaseRequest.js';

export default {
    data() {
        return {
			carts: [],
			subtotal: 0,
			data_search:""
        }
    },
	computed: {
        ...mapState(authStore, ['isLoggedIn', 'user'])
    },
	mounted() {
		this.getCarts()
	},
    methods: {
		...mapActions(authStore, ['clearAccessToken', 'clearUser', 'clearRefreshToken', 'clearProfile']),

		handleLogout: function() {
            this.clearAccessToken()
            this.clearRefreshToken()
            this.clearUser()
			this.clearProfile()
			mapState(authStore, ['isLoggedIn', 'user'])
			this.getCarts()
            this.$router.push({name: 'home'})
        },

		getCarts: function(){
			if (this.isLoggedIn) {
				this.subtotal = 0
				BaseRequest.get('orders/cart/list')
				.then(response => {
					this.carts = response.data
					for (const num in this.carts) {
						this.subtotal += this.carts[num].quantity * this.carts[num].product.price
					}
				})
				.catch(error=> {
					this.errors = error.response.data
					console.log("error")
				});
			}
        },

		Search: function() {
			this.$router.push({ name: 'search.list', params: { data_search: this.data_search } })
		}

    }
}
</script>

<style scoped>
</style>