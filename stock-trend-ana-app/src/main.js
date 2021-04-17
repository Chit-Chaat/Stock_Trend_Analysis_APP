import Vue from 'vue'
import router from './router'
import ElementUI from 'element-ui'
import App from './App.vue'
import axios from 'axios'
import locale from 'element-ui/lib/locale/lang/en'
import 'element-ui/lib/theme-chalk/index.css'
import 'vue-g2'
// import '@/assets/fonts/style.css'

Vue.config.productionTip = false
Vue.config.devtools = false;
Vue.prototype.$hostname = 'http://localhost:8000'

axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"
axios.defaults.xsrfCookieName = "csrftoken"
axios.defaults.withCredentials = true
axios.defaults.baseURL = Vue.prototype.$hostname

Vue.use(ElementUI, { locale });

export const bus = new Vue();

new Vue({
  el: '#app',
  router,
  render: h => h(App)
});
