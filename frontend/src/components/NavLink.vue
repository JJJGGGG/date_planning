<script setup lang="ts">
const props =  defineProps<{
  to: string
}>()
</script>

<template>
    <router-link :to="props.to">
      <button class="border-purple-600 cursor-pointer" :class="{ 'border-b-2': $route.path.startsWith(to) }">
        <slot />
      </button>
    </router-link>
</template>