<script setup lang="ts">
import NavbarComponent from '@/components/NavbarComponent.vue';
</script>

<template>
    <NavbarComponent />
    <div class="px-50 py-20"> 
        <router-view />
    </div>
</template>