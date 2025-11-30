<script setup lang="ts">
const props =  defineProps<{
  onClick?: () => void
}>()
</script>

<template>
    <button @click="props.onClick" type="button" class="cursor-pointer text-black">
        <slot />
    </button>
</template>