<script setup lang="ts">
import { usePlan } from '@/stores/usePlan';
import { usePlanRating } from '@/stores/usePlanRating';
import { usePlanRatings } from '@/stores/usePlanRatings';
import { computed, ref } from 'vue';
import { useRoute } from 'vue-router';

    const route = useRoute()

    // leer un parámetro
    const id = computed(() =>Number(route.params.id)); 

    const {plan} = usePlan(id);
    const {rating, addRating} = usePlanRating(id)
    const ratingM = ref(0)
    const {ratings} = usePlanRatings(id) // ojala unir esto con el de arriba
</script>


<template>
    <div class="text-xl">{{ plan?.activity }}</div>

    <div class="grid grid-cols-2">
        <div>Dirección</div>
        <div>{{ plan?.address }}</div>
        <div>Precio</div>
        <div>{{ plan?.price }}</div>
    </div>
    <div>Rating</div>
    <div>
        {{ rating?.rating ?? "no rating" }}
    </div>
    <input v-model="ratingM" />
    <button @click="() => addRating(ratingM)">AAAA</button>

    <div>
        <div v-for="other_rating in ratings">{{other_rating.user.email}} {{ other_rating.rating }}</div>
    </div>
    
</template>