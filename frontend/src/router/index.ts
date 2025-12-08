import { createRouter, createWebHistory } from 'vue-router'
import PlansView from "@/views/PlansView.vue"
import LoginView from '@/views/LoginView.vue'
import MainLayout from '@/layouts/MainLayout.vue'
import { useAuthStore } from '@/stores/useAuthStore'
import CreatePlanView from '@/views/CreatePlanView.vue'
import ViewUsersView from '@/views/ViewUsersView.vue'
import CreateUserView from '@/views/CreateUserView.vue'
import SinglePlanView from '@/views/SinglePlanView.vue'

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
          path: 'plans/:id',
          name: 'view_single_plan',
          component: SinglePlanView,
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
          meta: { onlyAnon: true }
        },
        {
          path: 'users',
          name: 'users',
          component: ViewUsersView,
          meta: { requiresAuth: true, requiresAdmin: true }
        },
        {
          path: 'users/create',
          name: 'create_user',
          component: CreateUserView,
          meta: { requiresAuth: true, requiresAdmin: true }
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

  // If the route requires auth and the user is NOT authenticated
  if (to.meta.requiresAuth && !auth.isAuthenticated) {
    return '/login'
  }

  if(to.meta.requiresAdmin && !auth.isAdmin) {
    return '/plans'
  }

  if(to.meta.onlyAnon && auth.isAuthenticated) {
    return '/plans'
  }
})

export default router
