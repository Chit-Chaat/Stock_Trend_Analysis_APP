import Vue from 'vue'
import Router from 'vue-router'
import Index from '../views/index'
import News from '../views/news'
import Support from '../views/support'
import About from '../views/about'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Index
    }, {
      path: '/index',
      name: 'Index',
      component: Index
    }, {
      path: '/news',
      name: 'News',
      component: News
    },
    {
      path: '/support',
      name: 'Support',
      component: Support
    }, {
      path: '/about',
      name: 'About',
      component: About
    }
  ]
})