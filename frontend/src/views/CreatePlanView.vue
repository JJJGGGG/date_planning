<script setup lang="ts">
import { useAuthStore } from '@/stores/useAuthStore';
import { useRouter } from 'vue-router';
import LabelComponent from '@/components/LabelComponent.vue'
import ButtonComponent from '@/components/ButtonComponent.vue'
import ErrorsComponent from '@/components/ErrorsComponent.vue'
import * as yup from 'yup';
import { useForm } from 'vee-validate';
import InputComponent from '@/components/InputComponent.vue';
import { usePlansStore } from '@/stores/usePlansStore';

const schema = yup.object({
  place: yup.string().required(),
  activity: yup.string().required(),
  type: yup.string().required(),
  address: yup.string().required(),
  price: yup.string().required(),
});

const plans = usePlansStore()

const router = useRouter()

const {handleSubmit, defineField, errors} = useForm<yup.InferType<typeof schema>>({
    validationSchema: schema
});

const onSubmit = handleSubmit(async (values) => {
    const success = await plans.create(
        values.place,
        values.activity,
        values.type,
        values.address,
        values.price
    )

    if(success) {
        router.push("/plans")
    }
});
const [place, placeAttrs] = defineField('place');
const [activity, activityAttrs] = defineField('activity');
const [type, typeAttrs] = defineField('type');
const [address, addressAttrs] = defineField('address');
const [price, priceAttrs] = defineField('price');

</script>

<template>
    <form @submit.prevent="onSubmit">
        <div>
            <LabelComponent for="activity">Actividad</LabelComponent>
            <InputComponent name="activity" v-model="activity" v-bind="activityAttrs" />
            <ErrorsComponent :value="errors.activity"/>
        </div>
        <div>
            <LabelComponent for="place">Lugar</LabelComponent>
            <InputComponent name="place" v-model="place" v-bind="placeAttrs" />
            <ErrorsComponent :value="errors.place"/>
        </div>
        <div>
            <LabelComponent for="type">Tipo</LabelComponent>
            <InputComponent name="type" v-model="type" v-bind="typeAttrs" />
            <ErrorsComponent :value="errors.type"/>
        </div>
        <div>
            <LabelComponent for="address">Dirección</LabelComponent>
            <InputComponent name="address" v-model="address" v-bind="addressAttrs" />
            <ErrorsComponent :value="errors.address"/>
        </div>
        <div>
            <LabelComponent for="price">Precio</LabelComponent>
            <InputComponent name="price" v-model="price" v-bind="priceAttrs" />
            <ErrorsComponent :value="errors.price"/>
        </div>
        <div>
            <ButtonComponent type="submit">Crear</ButtonComponent>
        </div>
    </form>
</template>