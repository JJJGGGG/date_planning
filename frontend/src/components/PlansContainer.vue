<script setup lang="ts">
import ButtonComponent from './ButtonComponent.vue';

</script>

<template>
<div class="flex justify-end">
    <RouterLink to="/plans/create">
        <ButtonComponent>Crear Plan</ButtonComponent>
    </RouterLink>
</div>
<div class="grid gap-4"> 
    <slot />
</div>
</template>