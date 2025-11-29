<script setup lang="ts">
import { useRouter } from 'vue-router';
import { useAuthStore } from './stores/useAuthStore';


const auth = useAuthStore()
const router = useRouter()
async function logout() {
  await auth.logout()
  router.push("/login")

}
</script>

<template>
  <button v-if="auth.isAuthenticated" @click="logout">Logout</button>
  {{ auth.user?.email }}
  <router-view />
</template>

<style scoped></style>
