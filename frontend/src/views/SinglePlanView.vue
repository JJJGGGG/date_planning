<script setup lang="ts">
import { usePlan } from '@/stores/usePlan';
import { usePlanRatings } from '@/stores/usePlanRatings';
import { computed, ref, unref } from 'vue';
import { useRoute } from 'vue-router';
import ChungungoRating from '@/components/ChungungoRating.vue';
import { useAuthStore } from '@/stores/useAuthStore';

    const route = useRoute()
    const auth = useAuthStore()

    const id = computed(() =>Number(route.params.id)); 

    const {plan} = usePlan(id);
    const {ratings, rating, addRating} = usePlanRatings(id)

    const other_peoples_ratings = computed(() => ratings.value.filter((r) => r.user_id != auth.user?.id))
</script>

<template>
    <div class="text-xl">{{ plan?.activity }}</div>

    <div class="grid grid-cols-2 mb-4">
        <div>Dirección</div>
        <div>{{ plan?.address }}</div>
        <div>Precio</div>
        <div>{{ plan?.price }}</div>
    </div>
    <div>
        Califica este plan:
    </div>
    <div class="px-4 py-4 border-4 border-gray-400 rounded-md bg-gray-200 inline-block">
        <ChungungoRating :rating="rating?.rating" :changeRating="addRating" />
    </div>
    <div class="mt-4">Otras calificaciones</div>
    <div>
        <div v-for="other_rating in other_peoples_ratings">
            <div>
                {{ other_rating.user.name }}
            </div>
            <ChungungoRating :disabled="true" :rating="other_rating.rating"/>
        </div>
        <div v-if="!other_peoples_ratings.length">
            No hay más calificaciones
        </div>
    </div>
    
</template>