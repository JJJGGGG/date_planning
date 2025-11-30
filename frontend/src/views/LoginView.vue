<script setup lang="ts">
import { useAuthStore } from '@/stores/useAuthStore';
import { useRouter } from 'vue-router';
import LabelComponent from '@/components/LabelComponent.vue'
import ButtonComponent from '@/components/ButtonComponent.vue'
import ErrorsComponent from '@/components/ErrorsComponent.vue'
import * as yup from 'yup';
import { Form, Field, ErrorMessage, useForm } from 'vee-validate';
import InputComponent from '@/components/InputComponent.vue';

const schema = yup.object({
  email: yup.string().required().email(),
  password: yup.string().required()
});

const auth = useAuthStore()

const router = useRouter()

const {handleSubmit, defineField, errors} = useForm<yup.InferType<typeof schema>>({
    validationSchema: schema
});

const onSubmit = handleSubmit(async (values) => {
    const success = await auth.login(values.email, values.password)

    if(success) {
        router.push("/plans")
    }
});
const [email, emailAttrs] = defineField('email');
const [password, passwordAttrs] = defineField('password');

</script>

<template>
    <form @submit.prevent="onSubmit">
        <div>
            <LabelComponent for="email">Email</LabelComponent>
            <InputComponent name="email" v-model="email" v-bind="emailAttrs" />
            <ErrorsComponent :value="errors.email"/>
        </div>
        <div>
            <LabelComponent for="password">Password</LabelComponent>
            <InputComponent name="password" type="password" v-model="password" v-bind="passwordAttrs" />
            <ErrorsComponent :value="errors.password"/>
        </div>
        <div>
            <ButtonComponent type="submit">Login</ButtonComponent>
        </div>
    </form>
</template>