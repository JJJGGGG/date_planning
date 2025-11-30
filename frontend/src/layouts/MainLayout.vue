<script setup lang="ts">
import { useRouter } from 'vue-router';
import { useAuthStore } from '@/stores/useAuthStore';
import NavButton from '@/components/NavButton.vue';

const auth = useAuthStore()
const router = useRouter()
async function logout() {
  await auth.logout()
  router.push("/login")

}
</script>

<template>
    <div class="shadow bg-gray-100 flex px-50 py-2">
        <div class="flex flex-grow">
            <button>Hola</button>
        </div>
        <div class="flex justify-end flex-grow">
            <NavButton v-if="auth.isAuthenticated" @click="logout">Logout</NavButton>
        </div>
    </div>
    <div class="px-50 py-20"> 
        <router-view />
    </div>
</template>