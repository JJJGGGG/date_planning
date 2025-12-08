<script setup lang="ts">
import { computed, ref, unref, watch } from 'vue';
import CabezaChungungo from './CabezaChungungo.vue';

    const CLASS_FULL = "full"
    const CLASS_MIDDLE = "half"
    const CLASS_EMPTY = "empty"

    const props = defineProps<{rating: number | undefined, changeRating?: (a: number) => void, disabled?: boolean}>()
    const rating = ref<number | undefined>(props.rating)
    watch(() => props.rating, (r) => rating.value = r)
    const displayRating = ref<number | undefined>(undefined);

    function getTypeForItem(pos: number) {
        let showedRating = undefined;
        if (rating.value) {
            showedRating = rating.value
        } else if(displayRating.value) {
            showedRating = displayRating.value;
        } 
        if(!showedRating) {
            return CLASS_EMPTY;
        }
        if(pos - 1 < Math.floor(showedRating)) {
            return CLASS_FULL;
        }
        if(Math.floor(showedRating) <= pos - 1 && pos - 1 < Math.ceil(showedRating)) {
            return CLASS_MIDDLE;
        }
        if(Math.ceil(showedRating) <= pos - 1) {
            return CLASS_EMPTY;
        }
        throw new Error("This is not implemented")
    }
</script>
<template>
    <div>
        <div v-for="i in 5" class="inline-block mr-2">
            <CabezaChungungo 
                :number="i" 
                :type="getTypeForItem(i)" 
                :setDisplayRating="(i: number | undefined) => {displayRating = i}" 
                :setRating="(i: number) => {changeRating && changeRating(i); rating = i}"
                :disabled="props.disabled"
            />
        </div>
    </div>
</template>