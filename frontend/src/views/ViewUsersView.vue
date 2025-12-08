<script setup lang="ts">
import { useUsersStore } from '@/stores/useUserStore';
import ButtonComponent from '@/components/ButtonComponent.vue';
import UserCard from "@/components/UserCard.vue"
    const users = useUsersStore();
    users.load();
</script>

<template>

<div class="flex justify-end pb-4">
    <RouterLink to="/users/create">
        <ButtonComponent>Crear Usuario</ButtonComponent>
    </RouterLink>
</div>
<div class="flex flex-col gap-4">
    <UserCard
        v-for="user in users.users"
        :name="user.name"
        :email="user.email"
        :is_admin="user.is_admin"
    />
</div>
</template>