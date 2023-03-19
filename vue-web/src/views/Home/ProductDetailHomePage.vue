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
                    <h3 class="breadcrumb-header">Sản phẩm</h3>
                <ul class="breadcrumb-tree">
                    <li>
                        <router-link :to="{name: 'home'}">Home</router-link>
                    </li>
                    <li class="active">{{ product.name }}</li>
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
                    <!-- Products tab & slick -->
					<div class="col-md-12">
						<div class="row">
							<!-- Product main img -->
                            <div class="col-md-5 col-md-push-2">
                                <div id="product-main-img">
                                    <div class="product-preview">
                                        <img :src="product.image" alt="">
                                    </div>
                                </div>
                            </div>
                            <!-- /Product main img -->

                            <!-- Product thumb imgs -->
                            <div class="col-md-2  col-md-pull-5">
                                <div id="product-imgs">
                                    <div class="product-preview">
                                        <img :src="product.image" alt="">
                                    </div>
                                </div>
                            </div>
                            <!-- /Product thumb imgs -->

                            <!-- Product details -->
                            <div class="col-md-5">
                                <div class="product-details">
                                    <h2 class="product-name">{{product.name}}</h2>
                                    <div>
                                        <h3 class="product-price">{{ product.price }} vnd</h3>
                                    </div>
                                    <p>{{ product.description }}</p>
                                    <div class="add-to-cart">
                                        <button class="add-to-cart-btn" @click="addToCart(product.id)"><i class="fa fa-shopping-cart"></i> add to cart</button>
                                    </div>
                                    <ul class="product-links">
                                        <li>Category:</li>
                                        <li><a href="#">{{ category.name }}</a></li>
                                    </ul>
									<ul class="product-links">
                                        <li>Brand:</li>
                                        <li><a href="#">{{ brand.name }}</a></li>
                                    </ul>
                                </div>
                            </div>
                            <!-- /Product details -->
							<!-- Product tab -->
								<div class="col-md-12">
									<div id="product-tab">
										<!-- product tab nav -->
										<ul class="tab-nav">
											<li class="active"><a data-toggle="tab" href="#tab1">Description</a></li>
											<li><a data-toggle="tab" href="#tab2">Comment</a></li>
											<li><a data-toggle="tab" href="#tab3">Reviews</a></li>
										</ul>
										<!-- /product tab nav -->

										<!-- product tab content -->
										<div class="tab-content">
											<!-- tab1  -->
											<div id="tab1" class="tab-pane fade in active">
												<div class="row">
													<div class="col-md-12">
														<p>{{ product.description }}</p>
													</div>
												</div>
											</div>
											<!-- /tab1  -->

											<!-- tab2  -->
											<div id="tab2" class="tab-pane fade in">
												<div class="row">
													<!-- Reviews -->
													<div class="col-md-9">
														<div id="reviews">
															<ul class="reviews">
																<li v-for="comment in product.comments_product" >
																	<div class="review-heading">
																		<h5 class="name">{{ comment.user }}</h5>
																		<p class="date">{{ comment.created_at }}</p>
																	</div>
																	<div class="review-body">
																		<p>{{ comment.comment }}</p>
																	</div>
																</li>
															</ul>
														</div>
													</div>
													<!-- /Reviews -->

													<!-- Review Form -->
													<div class="col-md-3">
														<div id="review-form">
															<textarea class="input" v-model="comment" placeholder="Your Comment"></textarea>					
															<button class="primary-btn" @click="Comment()">Submit</button>
														</div>
													</div>
													<!-- /Review Form -->
												</div>
											</div>
											<!-- /tab2  -->

											<!-- tab3  -->
											<div id="tab3" class="tab-pane fade in">
												<div class="row">
													<!-- Rating -->
													<div class="col-md-3">
														<div id="rating">
															<div class="rating-avg">
																<span>4.5</span>
																<div class="rating-stars">
																	<i class="fa fa-star"></i>
																	<i class="fa fa-star"></i>
																	<i class="fa fa-star"></i>
																	<i class="fa fa-star"></i>
																	<i class="fa fa-star-o"></i>
																</div>
															</div>
															<ul class="rating">
																<li>
																	<div class="rating-stars">
																		<i class="fa fa-star"></i>
																		<i class="fa fa-star"></i>
																		<i class="fa fa-star"></i>
																		<i class="fa fa-star"></i>
																		<i class="fa fa-star"></i>
																	</div>
																	<div class="rating-progress">
																		<div style="width: 80%;"></div>
																	</div>
																	<span class="sum">3</span>
																</li>
																<li>
																	<div class="rating-stars">
																		<i class="fa fa-star"></i>
																		<i class="fa fa-star"></i>
																		<i class="fa fa-star"></i>
																		<i class="fa fa-star"></i>
																		<i class="fa fa-star-o"></i>
																	</div>
																	<div class="rating-progress">
																		<div style="width: 60%;"></div>
																	</div>
																	<span class="sum">2</span>
																</li>
																<li>
																	<div class="rating-stars">
																		<i class="fa fa-star"></i>
																		<i class="fa fa-star"></i>
																		<i class="fa fa-star"></i>
																		<i class="fa fa-star-o"></i>
																		<i class="fa fa-star-o"></i>
																	</div>
																	<div class="rating-progress">
																		<div></div>
																	</div>
																	<span class="sum">0</span>
																</li>
																<li>
																	<div class="rating-stars">
																		<i class="fa fa-star"></i>
																		<i class="fa fa-star"></i>
																		<i class="fa fa-star-o"></i>
																		<i class="fa fa-star-o"></i>
																		<i class="fa fa-star-o"></i>
																	</div>
																	<div class="rating-progress">
																		<div></div>
																	</div>
																	<span class="sum">0</span>
																</li>
																<li>
																	<div class="rating-stars">
																		<i class="fa fa-star"></i>
																		<i class="fa fa-star-o"></i>
																		<i class="fa fa-star-o"></i>
																		<i class="fa fa-star-o"></i>
																		<i class="fa fa-star-o"></i>
																	</div>
																	<div class="rating-progress">
																		<div></div>
																	</div>
																	<span class="sum">0</span>
																</li>
															</ul>
														</div>
													</div>
													<!-- /Rating -->

													<!-- Reviews -->
													<div class="col-md-6">
														<div id="reviews">
															<ul class="reviews">
																<li>
																	<div class="review-heading">
																		<h5 class="name">John</h5>
																		<p class="date">27 DEC 2018, 8:0 PM</p>
																		<div class="review-rating">
																			<i class="fa fa-star"></i>
																			<i class="fa fa-star"></i>
																			<i class="fa fa-star"></i>
																			<i class="fa fa-star"></i>
																			<i class="fa fa-star-o empty"></i>
																		</div>
																	</div>
																	<div class="review-body">
																		<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua</p>
																	</div>
																</li>
																<li>
																	<div class="review-heading">
																		<h5 class="name">John</h5>
																		<p class="date">27 DEC 2018, 8:0 PM</p>
																		<div class="review-rating">
																			<i class="fa fa-star"></i>
																			<i class="fa fa-star"></i>
																			<i class="fa fa-star"></i>
																			<i class="fa fa-star"></i>
																			<i class="fa fa-star-o empty"></i>
																		</div>
																	</div>
																	<div class="review-body">
																		<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua</p>
																	</div>
																</li>
																<li>
																	<div class="review-heading">
																		<h5 class="name">John</h5>
																		<p class="date">27 DEC 2018, 8:0 PM</p>
																		<div class="review-rating">
																			<i class="fa fa-star"></i>
																			<i class="fa fa-star"></i>
																			<i class="fa fa-star"></i>
																			<i class="fa fa-star"></i>
																			<i class="fa fa-star-o empty"></i>
																		</div>
																	</div>
																	<div class="review-body">
																		<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua</p>
																	</div>
																</li>
															</ul>
															<ul class="reviews-pagination">
																<li class="active">1</li>
																<li><a href="#">2</a></li>
																<li><a href="#">3</a></li>
																<li><a href="#">4</a></li>
																<li><a href="#"><i class="fa fa-angle-right"></i></a></li>
															</ul>
														</div>
													</div>
													<!-- /Reviews -->

													<!-- Review Form -->
													<div class="col-md-3">
														<div id="review-form">
															<form class="review-form">
																<input class="input" type="text" placeholder="Your Name">
																<input class="input" type="email" placeholder="Your Email">
																<textarea class="input" placeholder="Your Review"></textarea>
																<div class="input-rating">
																	<span>Your Rating: </span>
																	<div class="stars">
																		<input id="star5" name="rating" value="5" type="radio"><label for="star5"></label>
																		<input id="star4" name="rating" value="4" type="radio"><label for="star4"></label>
																		<input id="star3" name="rating" value="3" type="radio"><label for="star3"></label>
																		<input id="star2" name="rating" value="2" type="radio"><label for="star2"></label>
																		<input id="star1" name="rating" value="1" type="radio"><label for="star1"></label>
																	</div>
																</div>
																<button class="primary-btn">Submit</button>
															</form>
														</div>
													</div>
													<!-- /Review Form -->
												</div>
											</div>
											<!-- /tab3  -->
										</div>
										<!-- /product tab content  -->
									</div>
								</div>
								<!-- /product tab -->
						</div>
					</div>
					<!-- Products tab & slick -->
				</div>
				<!-- /row -->
			</div>
			<!-- /container -->
		</div>
		<a-modal v-model:visible="visible_login" title="Ban chua dang nhap">
			<template #footer>
				<a-button key="login" type="primary" @click="handleLogin()">Dang nhap</a-button>
			</template>
		</a-modal>
	<!-- /SECTION -->

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
			product: {},
			visible_login: false,
			brand: {},
			category: {},
			comment: ""
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
			BaseRequest.get('products/product/detail/' + this.$route.params.product_id)
			.then(response => {
				this.product = response.data
				BaseRequest.get('products/category/detail/' + this.product.category)
				.then(response => {
					this.category = response.data
				})
				.catch(error=> {
					this.errors = error.response.data
				});

				BaseRequest.get('products/brand/detail/' + this.product.brand)
				.then(response => {
					this.brand = response.data
				})
				.catch(error=> {
					this.errors = error.response.data
				});
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

		Comment: function() {
			if (this.isLoggedIn) {
				BaseRequest.post('products/comment/create', {
					'product': this.product.id,
					'comment': this.comment
				})
				.then(response => {
					console.log(response.data)
					this.getProducts()
					this.createSuccessNotification('Thành công', 'Thêm bình luận thành công')
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