<script setup lang="ts">
import PlanCard from "@/components/PlanCard.vue";
import {usePlansStore} from "../stores/usePlansStore"
import PlansContainer from "@/components/PlansContainer.vue";
const plans = usePlansStore()

plans.load()
</script>

<template>
    <PlansContainer>
        <PlanCard 
        v-for="plan in plans.plans" 
        :key="plan.id"
        :place="plan.place"
        :type="plan.type"
        :price="plan.price"
        :activity="plan.activity"
        :address="plan.address"
        />
    </PlansContainer>
</template>