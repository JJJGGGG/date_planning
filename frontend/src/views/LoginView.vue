<script setup lang="ts">
import { useAuthStore } from '@/stores/useAuthStore';
import { ref } from 'vue';
import { useRouter } from 'vue-router';

const auth = useAuthStore()

const email = ref("")
const password = ref("")

const router = useRouter()

async function login() {
    const success = await auth.login(email.value, password.value)

    if(success) {
        router.push("/plans")
    }
}
</script>

<template>
    <div>{{ auth.user?.email }}</div>
    <div>
        <label>Email</label>
        <input v-model="email" />
    </div>
    <div>
        <label>Password</label>
        <input v-model="password" type="password" />
    </div>
    <div>
        <button @click="login">Login</button>
    </div>
</template>