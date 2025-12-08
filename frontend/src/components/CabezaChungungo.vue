<script setup lang="ts">
    import chungungo from "@/assets/chungungo.png"
    const props = defineProps<{
        type: "full" | "half" | "empty",
        number: number,
        setDisplayRating: (i: number | undefined) => void,
        setRating: (i: number) => void,
        disabled?: boolean
    }>()
</script>

<template>
    <div class="relative w-20 h-20">
        <div class="rating-item" :class="props.type">
            <img :src="chungungo" class="img-base" />
            <img :src="chungungo" class="img-left" />
        </div>
        <div class="absolute top-0 left-0 flex w-full h-full w-20 h-20">
            <div class="w-1/2 h-full" :class="{'cursor-pointer': !props.disabled}" @click="() => !props.disabled && setRating(props.number-0.5)" @mouseover="() => !props.disabled && setDisplayRating(props.number-0.5)" @mouseleave="() => !props.disabled && setDisplayRating(undefined)"></div>
            <div class="w-1/2 h-full" :class="{'cursor-pointer': !props.disabled}" @click="() => !props.disabled && setRating(props.number)" @mouseover="() => !props.disabled && setDisplayRating(props.number)" @mouseleave="() => !props.disabled && setDisplayRating(undefined)"></div>
        </div>
    </div>
</template>

<style>
.rating-item {
  position: relative;
  width: 100%;
  height: 100%;
}

/* BASE IMAGE: right side is dark */
.img-base {
  width: 100%;
  height: 100%;
  object-fit: contain;
  filter: brightness(0.4);   /* dark */
}

/* LEFT BRIGHT IMAGE */
.img-left {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: contain;
  filter: brightness(1.2);   /* bright */

  /* hidden unless type = half */
  opacity: 0;
  transition: opacity 0.15s ease-out;
}

/* only show left half of bright layer */
.rating-item.half .img-left {
  opacity: 1;
  clip-path: inset(0 50% 0 0); /* left half only */
}

/* Full rating = only bright image */
.rating-item.full .img-base {
  filter: brightness(1.2);
}

.rating-item.full .img-left {
  display: none;
}

/* Empty rating = fully dark */
.rating-item.empty .img-base {
  filter: brightness(0.3);
}

.rating-item.empty .img-left {
  display: none;
}
/* --- BORDER USING ALPHA CHANNEL --- */
.rating-item::after {
  content: "";
  position: absolute;
  inset: 0;

  /* Use the alpha channel of the PNG */
  -webkit-mask-image: url('/src/assets/chungungo.png');
  mask-image: url('/src/assets/chungungo.png');
  mask-size: contain;
  mask-repeat: no-repeat;

  border: 2px solid transparent;
  pointer-events: none;
  opacity: 0;
  transition: opacity 0.15s ease-out, clip-path 0.15s ease-out;
}

/* FULL BORDER */
.rating-item.full::after {
  opacity: 1;
  border-color: black;
  clip-path: inset(0);
}

/* HALF BORDER */
.rating-item.half::after {
  opacity: 1;
  border-color: black;
  clip-path: inset(0 50% 0 0); /* left half only */
}

/* EMPTY: no border */
.rating-item.empty::after {
  opacity: 0;
}
</style>