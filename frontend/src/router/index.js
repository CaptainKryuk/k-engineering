import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('../views/Home.vue')
  },

  {
    path: '/catalog',
    name: 'Catalog',
    component: () => import('../views/Catalog.vue')
  },

  // if collection is selected
  {
    path: '/catalog/:collection?',
    name: "Catalog",
    component: () => import('../views/Catalog.vue')
  },

  {
    path: '/test',
    name: 'Test',
    component: () => import('../views/other/Test.vue')
  },

  {
    path: '/materials/:item',
    name: 'DetailMaterial',
    component: () => import("../views/DetailMaterial.vue") 
  },

  {
    path: '/delivery',
    name: 'Delivery',
    component: () => import("../views/Delivery.vue")
  },

  {
    path: '/lk',
    name: 'Dashboard',
    component: () => import("../views/Dashboard.vue")
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
  scrollBehavior (to, from, savedPosition) {
    if (to.hash) {
      return {
        el: to.hash,
        behavior: 'smooth',
      }
    }
    return { top: 0}
  }
})

export default router
