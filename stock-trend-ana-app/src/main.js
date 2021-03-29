import Vue from 'vue'
import ElementUI from 'element-ui'
import App from './App.vue'
import locale from 'element-ui/lib/locale/lang/en'


import 'element-ui/lib/theme-chalk/index.css'

Vue.config.productionTip = false

Vue.use(ElementUI, { locale });

new Vue({
  el: '#app',
  render: h => h(App)
});
