<template>
    <link type="text/css" rel="stylesheet" href="css/bootstrap.min.css"/>
	<link rel="stylesheet" href="css/font-awesome.min.css">
	<link type="text/css" rel="stylesheet" href="css/style.css"/>
    <!-- /HEADER -->
    <HomeHeader/>   

    <a-form
        :model="user"
        name="basic"
        :label-col="{ span: 8 }"
        :wrapper-col="{ span: 8 }"
        autocomplete="off"
        @finish="signup"
        style="margin-top: 100px;"
    >
        <a-form-item
            label="Username"
            name="username"
            :rules="[{ required: true, message: 'Please input your username!' }]"
            >
            <a-input v-model:value="user.username" />
        </a-form-item>

        <a-form-item
            label="Password"
            name="password"
            :rules="[{ required: true, message: 'Please input your password!' }]"
            >
            <a-input-password v-model:value="user.password" />
        </a-form-item>

        <a-form-item
            label="Password2"
            name="password2"
            :rules="[{ required: true, message: 'Please input your password2!' }]"
            >
            <a-input-password v-model:value="user.password2" />
        </a-form-item>

        <a-form-item :wrapper-col="{ offset: 8, span: 16 }">
            <a-button type="primary" html-type="submit">Submit</a-button>

        </a-form-item>

    </a-form>
 

    <HomeFooter/>

</template>

<script>

import BaseRequest from '../../core/BaseRequest';
import { authStore } from '../../store/auth.store'
import { mapActions } from 'pinia';
import HomeHeader from '../../components/Home/HomeHeader.vue'
import HomeFooter from '../../components/Home/HomeFooter.vue'
import { notification } from 'ant-design-vue';


export default {
    data() {
        return {
            user: {
                username: "",
                password: "",
                password2: ""
            },
            errors: {}
        }
    },
    methods: {
        ...mapActions(authStore, ['setAccessToken', 'setUser', 'setRefreshToken', 'setProfile']),

        signup() {
            BaseRequest.post('users/register/customer', {
                username: this.user.username,
                password: this.user.password,
                password2: this.user.password2
            })
            .then(response => {
                console.log(response.data)
                this.createSuccessNotification('dang ky thanh cong', 'ok!')
                this.$router.push({name: 'login'});
            }).catch(error => {
                this.errors = error.response.data;
                console.log(this.errors)
                if (this.errors.password) {
                    this.errorsNotification('dang ky that bai', this.errors.password[0])
                }
                else 
                    this.errorsNotification('dang ky that bai', this.errors.username)
            });
        },

        errorsNotification: function(message, description) {
            notification['error']({
                message: message,
                description: description,
            });
        },

        createSuccessNotification: function(message, description) {
            notification['success']({
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