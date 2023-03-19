<template>
    <a-layout-header class="navbar-header">
        <a-row type="flex" justify="end" align="bottom">
            <a-col class="right-menu-header">
                <a-space :size="15">
                    <a-dropdown placement="bottomRight">
                        <a class="ant-dropdown-link" @click.prevent>
                            <a-avatar style="color: #f56a00; background-color: #fde3cf">U</a-avatar>
                        </a>

                        <template #overlay>
                            <a-menu>
                                <a-menu-item>Hi, {{ user.username }}</a-menu-item>
                                <!-- <a-menu-item>
                                    <router-link :to="{ name: 'account.detail', params: { username: user.username }}" >
                                        Profile
                                    </router-link>
                                </a-menu-item> -->
                                <a-menu-item @click="handleLogout">Logout</a-menu-item>
                            </a-menu>
                        </template>
                    </a-dropdown>
                </a-space>
            </a-col>
        </a-row>
    </a-layout-header>
</template>

<script>

import { authStore } from '../../store/auth.store'
import { mapActions, mapState } from 'pinia'
import { AppstoreOutlined, BellOutlined, MailOutlined } from '@ant-design/icons-vue'
export default {
    data() {
        return {
            carts: {},
            errors: {},
        }
    },
    computed: {
        ...mapState(authStore, ['user'])
    },
    mounted() {
    },
    methods: {
        ...mapActions(authStore, ['clearAccessToken', 'clearUser', 'clearRefreshToken', 'clearProfile']),
        handleLogout: function() {
            this.clearAccessToken()
            this.clearRefreshToken()
            this.clearUser()
            this.clearProfile()
            this.$router.push({name: 'home'})
        },
    },
    components: {
        AppstoreOutlined, BellOutlined, MailOutlined
    }
}
</script>

<style scoped>
.navbar-header {
    background-color: #fff;
    padding: 0 16px;
}
</style>