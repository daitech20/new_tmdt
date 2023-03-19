<template>
    <!-- /HEADER -->
	<div>
    <router-view v-slot="{ Component }">
        <!-- <transition> -->
            <component :is="Component" />
        <!-- </transition> -->
    </router-view>
  </div>
</template>

<script>
import { authStore } from './store/auth.store'
import { mapState } from 'pinia'

export default {
    data() {
        return {
        }
    },
    computed: {
        ...mapState(authStore, ['isLoggedIn', 'user'])
    }
    
}

</script>


<style scoped>
.content {
    margin: 0 16px;
}
</style>
1