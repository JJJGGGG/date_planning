<script setup lang="ts">
const props =  defineProps<{
  type?: 'button' | 'submit' | 'reset',
  onClick?: () => void
}>()
</script>

<template>
    <button @click="props.onClick" :type="type" class="px-2 py-1 border border-gray-400 rounded-md shadow text-white font-bold bg-purple-600 hover:bg-purple-500 cursor-pointer">
        <slot />
    </button>
</template>