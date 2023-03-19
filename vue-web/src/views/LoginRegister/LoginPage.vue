<template>
    <link type="text/css" rel="stylesheet" href="css/bootstrap.min.css"/>
	<link rel="stylesheet" href="css/font-awesome.min.css">
	<link type="text/css" rel="stylesheet" href="css/style.css"/>
    <!-- /HEADER -->
    <HomeHeader/>   

    <a-form
        :model="credentials"
        name="basic"
        :label-col="{ span: 8 }"
        :wrapper-col="{ span: 8 }"
        autocomplete="off"
        @finish="login"
        style="margin-top: 100px;"
    >
        <a-form-item
        label="Username"
        name="username"
        :rules="[{ required: true, message: 'Please input your username!' }]"
        >
        <a-input v-model:value="credentials.username" />
        </a-form-item>
        <a-form-item
        label="Password"
        name="password"
        :rules="[{ required: true, message: 'Please input your password!' }]"
        >
        <a-input-password v-model:value="credentials.password" />
        </a-form-item>

        <a-form-item :wrapper-col="{ offset: 8, span: 16 }">
            <a-button type="primary" html-type="submit">Login</a-button>

            <router-link :to="{ name: 'signup'}" >
                <a-button type="primary" style="margin-left: 100px;" >Signup</a-button>
            </router-link>
        </a-form-item>

    </a-form>
 

    <HomeFooter/>

</template>

<script>

import authService from '../../services/auth.service'
import { authStore } from '../../store/auth.store'
import { mapActions } from 'pinia';
import HomeHeader from '../../components/Home/HomeHeader.vue'
import HomeFooter from '../../components/Home/HomeFooter.vue'
import { notification } from 'ant-design-vue';


export default {
    data() {
        return {
            credentials: {
                username: "",
                password: ""
            },
            errors: {}
        }
    },
    methods: {
        ...mapActions(authStore, ['setAccessToken', 'setUser', 'setRefreshToken', 'setProfile']),

        login() {
            authService.login(this.credentials.username, this.credentials.password).then(response => {
              console.log(response.data)
              this.setAccessToken(response.data.access);
                this.setRefreshToken(response.data.refresh);
                this.setUser(response.data.user);
                if (response.data.profile) {
                    this.setProfile(response.data.profile);
                }
                this.$router.push({name: 'home'});
            }).catch(error => {
                this.errors = error.response.data;
                console.log(this.errors)
                this.errorsNotification('dang nhap that bai', 'sai mat khau')
            });
        },

        errorsNotification: function(message, description) {
            notification['error']({
                message: message,
                description: description,
            });
        }
    },
    components: {
        HomeHeader,
        HomeFooter
    }
}
</script>

<style scoped>

</style>