<script setup lang="ts">
import GenericCard from './GenericCard.vue';
import CardAction from './CardAction.vue';
const { place, address, price, activity, id } = defineProps<{
    place: string,
    activity: string,
    type: string,
    address: string,
    price: string,
    id: number
}>()
</script>

<template>
    <GenericCard :title="activity">
        <div>Lugar: {{ place }}</div>
        <div>Dirección: {{ address }}</div>
        <div>Precio: {{ price }}</div>
        <template #actions>
            <CardAction :to="`/plans/${id}`" icon="Ver" />
        </template>
    </GenericCard>
</template>