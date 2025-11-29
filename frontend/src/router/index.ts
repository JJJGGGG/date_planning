import { createRouter, createWebHistory } from 'vue-router'
import PlansView from "@/views/PlansView.vue"
import LoginView from '@/views/LoginView.vue'
import MainLayout from '@/layouts/MainLayout.vue'
import { useAuthStore } from '@/stores/useAuthStore'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      component: MainLayout,
      children:[
        {
          path: '/plans',
          name: 'plans',
          component: PlansView,
          meta: { requiresAuth: true }
        },
        {
          path: '/login',
          name: 'login',
          component: LoginView,
          meta: { requiresAuth: false }
        },
      ]
    }
  ],
})

router.beforeEach(async (to) => {
  const auth = useAuthStore();
  await auth.get_data();

  // If the route requires auth and the user is NOT authenticated
  if (to.meta.requiresAuth && !auth.isAuthenticated) {
    return '/login'
  }
})

export default router
