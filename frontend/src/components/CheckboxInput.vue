<script setup lang="ts">
    const props = defineProps<{
        name: string,
        label: string
    }>()

    const model = defineModel<boolean>()
</script>

<template>
    <label :for="props.name">
        <input type="checkbox" :name="props.name" v-model="model"/>
        {{ props.label }}
    </label>
</template>