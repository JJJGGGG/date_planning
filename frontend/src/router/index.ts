import { createRouter, createWebHistory } from 'vue-router'
import PlansView from "@/views/PlansView.vue"
import LoginView from '@/views/LoginView.vue'
import MainLayout from '@/layouts/MainLayout.vue'
import { useAuthStore } from '@/stores/useAuthStore'
import CreatePlanView from '@/views/CreatePlanView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      component: MainLayout,
      children:[
        {
          path: '/',
          name: 'index',
          redirect: "/plans",
          meta: { requiresAuth: true }
        },
        {
          path: 'plans',
          name: 'plans',
          component: PlansView,
          meta: { requiresAuth: true }
        },
        {
          path: 'plans/create',
          name: 'create_plan',
          component: CreatePlanView,
          meta: { requiresAuth: true }
        },
        {
          path: 'login',
          name: 'login',
          component: LoginView,
          meta: { requiresAuth: false }
        },
      ]
    },
    {
      path: '/:pathMatch(.*)*',
      name: 'NotFound',
      redirect: '/plans',
      meta: { requiresAuth: false },
    },
  ],
})

router.beforeEach(async (to) => {
  const auth = useAuthStore();
  await auth.get_data();

  console.log(auth.isAuthenticated, to.meta.requiresAuth)

  // If the route requires auth and the user is NOT authenticated
  if (to.meta.requiresAuth && !auth.isAuthenticated) {
    return '/login'
  }
})

export default router
