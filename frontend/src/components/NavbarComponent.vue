<script setup lang="ts">
import { useRouter } from 'vue-router';
import { useAuthStore } from '@/stores/useAuthStore';
import NavButton from '@/components/NavButton.vue';
import NavLink from './NavLink.vue';

const auth = useAuthStore()
const router = useRouter()
async function logout() {
  await auth.logout()
  router.push("/login")

}
</script>

<template>
    <div class="shadow bg-gray-100 flex px-50 py-2">
        <div class="flex flex-grow gap-2">
            <NavLink to="/plans">
                Planes
            </NavLink>
            <NavLink v-show="auth.isAdmin" to="/users">
                Usuarios
            </NavLink>
        </div>
        <div class="flex justify-end flex-grow">
            <NavButton v-show="auth.isAuthenticated" @click="logout">Logout</NavButton>
        </div>
    </div>
</template>