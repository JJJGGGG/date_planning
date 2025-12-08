<script setup lang="ts">
import { useRouter } from 'vue-router';
import LabelComponent from '@/components/LabelComponent.vue'
import ButtonComponent from '@/components/ButtonComponent.vue'
import ErrorsComponent from '@/components/ErrorsComponent.vue'
import * as yup from 'yup';
import { useForm } from 'vee-validate';
import InputComponent from '@/components/InputComponent.vue';
import { useUsersStore } from '@/stores/useUserStore';
import CheckboxInput from '@/components/CheckboxInput.vue';

const schema = yup.object({
  name: yup.string().required(),
  password: yup.string().required(),
  email: yup.string().email().required(),
  is_admin: yup.boolean().default(false),
});

const users = useUsersStore()

const router = useRouter()

const {handleSubmit, defineField, errors} = useForm<yup.InferType<typeof schema>>({
    validationSchema: schema
});

const onSubmit = handleSubmit(async (values) => {
    console.log(values)
    const success = await users.create(
        values.name,
        values.email,
        values.password,
        values.is_admin
    )

    if(success) {
        router.push("/users")
    }
});
const [email, emailAttrs] = defineField('email');
const [name, nameAttrs] = defineField('name');
const [password, passwordAttrs] = defineField('password');
const [is_admin, is_adminAttrs] = defineField('is_admin');

</script>

<template>
    <form @submit.prevent="onSubmit">
        <div>
            <LabelComponent for="name">Nombre</LabelComponent>
            <InputComponent name="name" v-model="name" v-bind="nameAttrs" />
            <ErrorsComponent :value="errors.name"/>
        </div>
        <div>
            <LabelComponent for="email">Email</LabelComponent>
            <InputComponent name="email" v-model="email" v-bind="emailAttrs" />
            <ErrorsComponent :value="errors.email"/>
        </div>
        <div>
            <LabelComponent for="password">Contraseña</LabelComponent>
            <InputComponent name="password" type="password" v-model="password" v-bind="passwordAttrs" />
            <ErrorsComponent :value="errors.password"/>
        </div>
        <div>
            <CheckboxInput name="is_admin" v-model="is_admin" v-bind="is_adminAttrs" label="Admin" />
            <ErrorsComponent :value="errors.is_admin"/>
        </div>
        <div>
            <ButtonComponent type="submit">Crear</ButtonComponent>
        </div>
    </form>
</template>