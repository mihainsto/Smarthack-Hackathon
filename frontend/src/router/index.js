import Vue from 'vue'
import Router from 'vue-router'
import VueCookie from 'vue-cookie';

import HomePage from '@/components/HomePage'
import LoginPage from '@/components/Login'
import Logout from '@/components/Logout'
import RegisterPage from '@/components/Register'
import Ofer from '@/components/Ofer'
import Anunt from '@/components/Anunt'
import Anunturi from '@/components/Anunturi'
import Alerte from '@/components/Alerte'

Vue.use(Router)
Vue.use(VueCookie)

export default new Router({
  mode: 'history',
  routes: 
  [
    { path: '/', component: HomePage }, 
    { path: '/ofer', component: Ofer }, 
    { path: '/login', component: LoginPage },
    { path: '/register', component: RegisterPage },
    { path: '/logout', component: Logout },
    { path: '/anunt/:id', component: Anunt},
    { path: '/anunturi', component: Anunturi},
    { path: '/alerte', component: Alerte}
  ]
})
