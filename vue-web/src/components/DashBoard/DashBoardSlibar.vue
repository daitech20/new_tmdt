<template>
    <a-layout-sider v-model="collapsed">
        <div class="logo">
        </div>
        <a-menu theme="dark" mode="inline">
            <a-sub-menu key="keyword" v-if="user && user.is_superuser">
                <template #title>
                    <span>
                        <read-outlined />
                        <span>Keyword</span>
                    </span>
                </template>
                <a-menu-item key="keyword.list" >
                    <unordered-list-outlined />
                    <router-link class="menu-link" :to="{name: 'keyword.list'}">Keywords</router-link>
                </a-menu-item>

                <a-menu-item key="keyword.create" >
                    <plus-circle-outlined />
                    <router-link class="menu-link" :to="{name: 'keyword.create'}">Add keyword</router-link>
                </a-menu-item>
                
            </a-sub-menu>

            <a-sub-menu key="category" v-if="user && user.is_superuser">
                <template #title>
                    <span>
                        <appstore-add-outlined />
                        <span>Category</span>
                    </span>
                </template>
                <a-menu-item key="category.list" >
                    <unordered-list-outlined />
                    <router-link class="menu-link" :to="{name: 'category.list'}">Categories</router-link>
                </a-menu-item>

                <a-menu-item key="category.create" >
                    <plus-circle-outlined />
                    <router-link class="menu-link" :to="{name: 'category.create'}">Add category</router-link>
                </a-menu-item>
                
            </a-sub-menu>

            <a-sub-menu key="brand" v-if="user && user.is_superuser">
                <template #title>
                    <span>
                        <book-outlined />
                        <span>Brand</span>
                    </span>
                </template>
                <a-menu-item key="brand.list" >
                    <unordered-list-outlined />
                    <router-link class="menu-link" :to="{name: 'brand.list'}">Brands</router-link>
                </a-menu-item>

                <a-menu-item key="brand.create" >
                    <plus-circle-outlined />
                    <router-link class="menu-link" :to="{name: 'brand.create'}">Add brand</router-link>
                </a-menu-item>
                
            </a-sub-menu>

            <a-sub-menu key="product" v-if="user && user.is_superuser">
                <template #title>
                    <span>
                        <gold-outlined />
                        <span>Product</span>
                    </span>
                </template>
                <a-menu-item key="product.list" >
                    <unordered-list-outlined />
                    <router-link class="menu-link" :to="{name: 'product.list'}">Products</router-link>
                </a-menu-item>
                
            </a-sub-menu>

            <a-menu-item key="order.list">
                <gold-outlined/>
                <router-link class="menu-link" :to="{name: 'order.list'}">Đơn hàng</router-link>
            </a-menu-item>

        </a-menu>
    </a-layout-sider>
</template>

<script>

import { authStore } from '../../store/auth.store'
import { mapState } from 'pinia'
import BaseRequest from '../../core/BaseRequest.js'
import { 
    PieChartOutlined,
    UserOutlined, 
    MessageOutlined,
    GoldOutlined,
    PayCircleOutlined,
    OrderedListOutlined,
    UnorderedListOutlined,
    ReadOutlined,
    PlusCircleOutlined,
    AppstoreAddOutlined,
    BookOutlined
} from '@ant-design/icons-vue'


export default {
    data() {
        return {
            selectedKeys: [],
            collapsed: false,
            errors: {
            }
        }
    },

    computed: {
        ...mapState(authStore, ['user'])
    },

    methods: {

    },

    components: {
        PieChartOutlined,
        UserOutlined,
        MessageOutlined,
        GoldOutlined,
        PayCircleOutlined,
        OrderedListOutlined,
        UnorderedListOutlined,
        ReadOutlined,
        PlusCircleOutlined,
        AppstoreAddOutlined,
        BookOutlined
    }
}
</script>

<style scoped>
.logo {
    width: 100%;
    padding: 16px 16px;
}
.logo-image {
   width: 100%;
   background-color: #fff;
}
.ant-menu-item .anticon + .menu-link {
    margin-left: 10px;
}
.ant-menu.ant-menu-inline-collapsed > .ant-menu-item .anticon + .menu-link {
    display: inline-block;
    opacity: 0;
}
</style>