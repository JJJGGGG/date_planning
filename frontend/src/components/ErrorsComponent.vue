<script setup lang="ts">
const props =  defineProps<{
  value: string | undefined
}>()
</script>


<template>
<div>
    <span class="text-red-500">{{ value }}<span class="text-transparent">a</span></span>
</div>
</template>