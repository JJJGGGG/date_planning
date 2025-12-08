<script setup lang="ts">
import PlanCard from "@/components/PlanCard.vue";
import ButtonComponent from '@/components/ButtonComponent.vue';
import {usePlansStore} from "../stores/usePlansStore"
const plans = usePlansStore()

plans.load()
</script>

<template>
<div class="flex justify-end pb-4">
    <RouterLink to="/plans/create">
        <ButtonComponent>Crear Plan</ButtonComponent>
    </RouterLink>
</div>

<div class="flex flex-col gap-4"> 
    <PlanCard 
        v-for="plan in plans.plans" 
        :key="plan.id"
        :id="plan.id"
        :place="plan.place"
        :type="plan.type"
        :price="plan.price"
        :activity="plan.activity"
        :address="plan.address"
    />
</div>
</template>