<script setup lang="ts">
import { useAuthStore } from './stores/useAuthStore';


const auth = useAuthStore()

async function logout() {
  await auth.logout()
}
</script>

<template>
  <button @click="logout">Logout</button>
  {{ auth.user?.email }}
  <router-view />
</template>

<style scoped></style>
