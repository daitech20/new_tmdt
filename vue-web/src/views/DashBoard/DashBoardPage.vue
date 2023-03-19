<template>
    <a-layout v-if="isLoggedIn" style="min-height: 100vh">
        <DashBoardSlibar/>
        <a-layout>
            <DashBoardHeader/>
                <a-layout-content class="content">
                    <router-view v-slot="{ Component }">
                        <!-- <transition> -->
                            <component :is="Component" />
                        <!-- </transition> -->
                    </router-view>
                </a-layout-content>
            <DashBoardFooter/>
        </a-layout>
    </a-layout>
</template>

<script>
import DashBoardSlibar from '../../components/DashBoard/DashBoardSlibar.vue'
import DashBoardHeader from '../../components/DashBoard/DashBoardHeader.vue'
import DashBoardFooter from '../../components/DashBoard/DashBoardFooter.vue'
import { authStore } from '../../store/auth.store'
import { mapState } from 'pinia'


export default {
    data() {
        return {
        }
    },

    components: {
        DashBoardSlibar, DashBoardHeader, DashBoardFooter
    },

    computed: {
        ...mapState(authStore, ['isLoggedIn', 'user']),
    },

    mounted() {
        this.checkIsLoggedIn()
    },

    methods: {
        checkIsLoggedIn: function() {
            if (this.isLoggedIn == false) {
                this.$router.push({name: 'home'})
            }
        }
    }

    
}
</script>