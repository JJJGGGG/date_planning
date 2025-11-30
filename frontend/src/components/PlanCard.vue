<script setup lang="ts">
const { place } = defineProps<{
    place: string,
    activity: string,
    type: string,
    address: string,
    price: string
}>()
</script>

<template>
    <div class="rounded border border-1 border-gray-500">
        <div className="bg-gray-500 text-white font-bold px-4 py-2">
            {{ activity }}
        </div>
        <div className="px-4 py-2">
            <div>Lugar: {{ place }}</div>
            <div>Dirección: {{ address }}</div>
            <div>Precio: {{ price }}</div>
        </div>
    </div>
</template>