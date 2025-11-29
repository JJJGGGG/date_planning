<script setup lang="ts">
const props =  defineProps<{
  title: string
  type?: 'button' | 'submit' | 'reset',
  click?: () => void
}>()
</script>

<template>
    <button @click="props.click" :type="type" class="px-2 py-1 border border-gray-400 rounded-md shadow bg-blue-400 hover:bg-blue-300 cursor-pointer">
        {{ props.title }}
    </button>
</template>