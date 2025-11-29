import type { User } from '@/models/user';
import { defineStore } from 'pinia'

export const useAuthStore = defineStore('auth', {
  state: () => ({
    user: null as null | User,
    isAuthenticated: false,
    loading: false,
  }),

  actions: {
    async login(email: string, password: string) {

      try {
        this.loading = true
        const request = await fetch('http://localhost:8000/user/login', {
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
      if(this.isAuthenticated) {
        return;
      }
      const request = await fetch('http://localhost:8000/user/me', {
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

    },

    async logout() {
      await fetch('http://localhost:8000/user/logout', {
        method: "post",
        credentials: "include"
      })
      this.user = null
      this.isAuthenticated = false
    },
  },
})