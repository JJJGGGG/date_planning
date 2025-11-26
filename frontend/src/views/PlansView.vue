<script setup lang="ts">
import {usePlansStore} from "../stores/usePlansStore"
const plans = usePlansStore()

plans.load()
</script>

<template>
    <div>
        <div 
        v-for="plan in plans.plans" 
        :key="plan.id"
        class="plan-item"
        >
            {{plan.place}}
        </div>
    </div>
</template>