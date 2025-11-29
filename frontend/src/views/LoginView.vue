<script setup lang="ts">
import { useAuthStore } from '@/stores/useAuthStore';
import { useRouter } from 'vue-router';
import ButtonComponent from '@/components/ButtonComponent.vue'
import * as yup from 'yup';
import { Form, Field, ErrorMessage } from 'vee-validate';

const schema = yup.object({
  email: yup.string().required().email(),
  password: yup.string().required()
});

const auth = useAuthStore()

const router = useRouter()

async function login(values: yup.InferType<typeof schema>) {
    const success = await auth.login(values.email, values.password)

    if(success) {
        router.push("/plans")
    }
}

</script>

<template>
    <Form @submit="login" :validation-schema="schema">
        <Field name="email" type="email" />
        <ErrorMessage name="email" />

        <Field name="password" type="password" />
        <ErrorMessage name="password" />

        <ButtonComponent title="Login" type="submit"></ButtonComponent>
    </Form>
</template>