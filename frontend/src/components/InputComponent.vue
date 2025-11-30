<script setup lang="ts">
const model = defineModel<string>()
const props = defineProps<{name: string, type?: string}>()
</script>

<template>
    <input v-model="model" :name="name" :type="type" class="border border-1 border-gray-300 rounded-md px-2" />
</template>