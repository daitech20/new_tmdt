import { createApp } from 'vue'
import App from './App.vue'
import { createPinia } from 'pinia'
import router from './routers'
import Antd from 'ant-design-vue'
import 'ant-design-vue/dist/antd.css'
import './assets/css/bootstrap.min.css'
import './assets/css/font-awesome.min.css'
import './assets/css/style.css'
import './assets/js/jquery.min.js'
import './assets/js/bootstrap.min.js'
import './assets/js/slick.min.js'
import './assets/js/nouislider.min.js'
import './assets/js/jquery.zoom.min.js'
import './assets/js/main.js'

const app = createApp(App)
app.use(createPinia())
app.use(Antd)
app.use(router)
app.mount('#app')
