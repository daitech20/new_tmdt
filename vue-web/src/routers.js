import { createRouter, createWebHistory } from "vue-router"
import { authStore } from "./store/auth.store"
import HomePage from "./views/Home/HomePage.vue"
import LoginPage from './views/LoginRegister/LoginPage.vue'
import SignupPage from './views/LoginRegister/SignupPage.vue'
import DashboardPage from './views/DashBoard/DashBoardPage.vue'
import KeywordListPage from './views/Keyword/KeywordListPage.vue'
import KeywordCreatePage from './views/Keyword/KeywordCreatePage.vue'
import KeywordDetailPage from './views/Keyword/KeywordDetailPage.vue'
import CategoryListPage from './views/Category/CategoryListPage.vue'
import CategoryCreatePage from './views/Category/CategoryCreatePage.vue'
import CategoryDetailPage from './views/Category/CategoryDetailPage.vue'
import BrandListPage from './views/Brand/BrandListPage.vue'
import BrandDetailPage from './views/Brand/BrandDetailPage.vue'
import BrandCreatePage from './views/Brand/BrandCreatePage.vue'
import ProductListPage from './views/Product/ProductListPage.vue'
import ProductCreatePage from './views/Product/ProductCreatePage.vue'
import ProductDetailPage from './views/Product/ProductDetailPage.vue'
import CartPage from './views/Home/CartPage.vue'
import CheckoutPage from './views/Home/CheckoutPage.vue'
import DashBoardOrderPage from './views/DashBoard/DashBoardOrderPage.vue'
import DashBoardOrderDetailPage from './views/DashBoard/DashBoardOrderDetailPage.vue'
import SearchPage from './views/Home/SearchPage.vue'
import ProductDetailHomePage from './views/Home/ProductDetailHomePage.vue'
// import AccountListPage from './views/account/AccountListPage.vue'
// import AccountCreatePage from './views/account/AccountCreatePage.vue'
// import AccountDetailPage from './views/account/AccountDetailPage.vue'
// import AccountChangePasswordPage from './views/account/AccountChangePasswordPage.vue'
// import AccountResetPasswordPage from './views/account/AccountResetPasswordPage.vue'


const routes = [
    {
        name: 'home',
        path: '/',
        component: HomePage
    },
    {
        name: 'login',
        path: '/login',
        component: LoginPage
    },
    {
        name: 'signup',
        path: '/signup',
        component: SignupPage
    },
    {
        name: 'dashboard',
        path: '/dashboard',
        component: DashboardPage,
        params: true
    },
    {
        name: 'keyword.list',
        path: '/dashboard/keywords',
        component: KeywordListPage,
        params: true
    },
    {
        name: 'keyword.create',
        path: '/dashboard/keyword/create',
        component: KeywordCreatePage,
        params: true
    },
    {
        name: 'keyword.detail',
        path: '/dashboard/keyword/detail/:keyword_id',
        component: KeywordDetailPage,
        params: true
    },
    {
        name: 'category.list',
        path: '/dashboard/categories',
        component: CategoryListPage,
        params: true
    },
    {
        name: 'category.create',
        path: '/dashboard/category/create',
        component: CategoryCreatePage,
        params: true
    },
    {
        name: 'category.detail',
        path: '/dashboard/category/detail/:category_id',
        component: CategoryDetailPage,
        params: true
    },
    {
        name: 'brand.list',
        path: '/dashboard/brands',
        component: BrandListPage,
        params: true
    },
    {
        name: 'brand.create',
        path: '/dashboard/brand/create',
        component: BrandCreatePage,
        params: true
    },
    {
        name: 'brand.detail',
        path: '/dashboard/brand/detail/:brand_id',
        component: BrandDetailPage,
        params: true
    },
    {
        name: 'product.list',
        path: '/dashboard/products',
        component: ProductListPage,
        params: true
    },
    {
        name: 'product.create',
        path: '/dashboard/product/create',
        component: ProductCreatePage,
        params: true
    },
    {
        name: 'product.detail',
        path: '/dashboard/product/detail/:product_id',
        component: ProductDetailPage,
        params: true
    },
    {
        name: 'cart.list',
        path: '/carts',
        component: CartPage,
        params: true
    },
    {
        name: 'checkout',
        path: '/checkout',
        component: CheckoutPage,
        params: true
    },
    {
        name: 'order.list',
        path: '/orders',
        component: DashBoardOrderPage,
        params: true
    },
    {
        name: 'order.detail',
        path: '/order/detail/:order_id',
        component: DashBoardOrderDetailPage,
        params: true
    },
    {
        name: 'search.list',
        path: '/search/:data_search',
        component: SearchPage,
        params: true
    },
    {
        name: 'product.home.detail',
        path: '/product/:product_id',
        component: ProductDetailHomePage,
        params: true
    },
]

const router = createRouter({
    // 4. Provide the history implementation to use. We are using the hash history for simplicity here.
    history: createWebHistory(),
    routes // short for `routes: routes`
})

export default router