import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/HomeView.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/home#contact',  // Utiliser le chemin avec un hash
    redirect: { path: '/', hash: '#contact' }  // Redirection vers la Home avec le hash
  },
  {path: "/login", component: () => import("../views/LoginView.vue")},
  {path: "/sign-up", component: () => import("../views/SignUpView.vue")},
  {path: "/generate", component: () => import("../views/GenerationView.vue")},
  {path: "/history", component: () => import("../views/HistoryView.vue")},
  {path: "/past-generations", component: () => import("../views/PastGenerationsView.vue")},
]

const router = createRouter({
  history: createWebHistory('/'),
  routes
})

export default router