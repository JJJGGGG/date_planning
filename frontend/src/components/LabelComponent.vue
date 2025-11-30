<script setup lang="ts">
const {for: _for} =  defineProps<{
  for: string
}>()
</script>


<template>
<div>
    <label :for="_for" class="text-red"><slot /></label>
</div>
</template>