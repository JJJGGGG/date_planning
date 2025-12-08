<script setup lang="ts">
    const { title } = defineProps<{title: string}>()
</script>

<template>
    <div class="rounded border border-1 border-gray-500">
        <div class="bg-gray-500 text-white font-bold px-4 py-2 flex justify-between">
            <div>
                {{ title }}
            </div>
            <div>
                <slot name="actions"></slot>
            </div>
        </div>
        <div className="px-4 py-2">
            <slot></slot>
        </div>
    </div>
</template>