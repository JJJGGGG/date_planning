import type { User } from '@/models/user';
import { defineStore } from 'pinia'

export const useAuthStore = defineStore('auth', {
  state: () => ({
    user: null as null | User,
    isAuthenticated: false,
    loading: false,
    expires: 0
  }),

  actions: {
    async login(email: string, password: string) {

      try {
        this.loading = true
        const request = await fetch(`${import.meta.env.VITE_BACKEND_URL}/user/login`, {
          method: "post",
          credentials: "include",
          headers: {
            "content-type": "application/json"
          },
          body: JSON.stringify({
            email,
            password,
          })
        })


        if(!request.ok) {
          return false;
        }

        this.loading = false;

        await this.get_data()

        return true
      } catch {
        this.loading = false
        return false;
      }
    },

    async get_data() {
      if(this.expires < Date.now()) {
        this.user = null;
        this.isAuthenticated = false;
      }
      if(this.isAuthenticated) {
        return;
      }
      const request = await fetch(`${import.meta.env.VITE_BACKEND_URL}/user/me`, {
        method: "get",
        credentials: 'include'
      })

      if(!request.ok) {
        this.user = null;
        this.isAuthenticated = false;
        return;
      }

      const user: User = await request.json()

      this.user = user;
      this.isAuthenticated = true;
      this.expires = user.expires;

    },

    async logout() {
      await fetch(`${import.meta.env.VITE_BACKEND_URL}/user/logout`, {
        method: "post",
        credentials: "include"
      })
      this.user = null
      this.isAuthenticated = false
    },
  },
})