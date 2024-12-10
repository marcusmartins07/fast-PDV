import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Pedido from '../views/Pedido.vue'
import Venda from '../views/Venda.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/home',
      name: 'Home',
      component: Home
    },
    {
      path: '/',
      name: 'Venda',
      meta: { requiresAuth: true },
      component: Venda
    },
    {
      path: '/pedido',
      name: 'Pedido',
      meta: { requiresAuth: true },
      component: Pedido
    }
  ]
})

router.beforeEach((to, from, next) => {
  const accessToken = localStorage.getItem('accessToken');
  if (to.matched.some((record) => record.meta.requiresAuth) && !accessToken) {
    next({ name: 'Home' });
  } else {
    next();
  }
});

export default router
