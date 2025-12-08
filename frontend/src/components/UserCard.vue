<script setup lang="ts">
    import GenericCard from './GenericCard.vue';
    const props = defineProps<{
        name: string,
        is_admin: boolean,
        email: string
    }>()
</script>

<template>
    <GenericCard :title="props.name">
        <div>
            {{ props.email }}
        </div>
        <div>
            {{ props.is_admin ? "Admin" : "User" }}
        </div>
    </GenericCard>
</template>