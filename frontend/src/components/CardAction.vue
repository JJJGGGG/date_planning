<script setup lang="ts">
    const props = defineProps<{to: string, icon: string}>();
</script>

<template>
    <router-link :to="props.to">
        {{ props.icon }}
    </router-link>
</template>