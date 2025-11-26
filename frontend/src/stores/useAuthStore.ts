import { defineStore } from 'pinia'

export const useAuthStore = defineStore('auth', {
  state: () => ({
    user: null as null | { name: string, email: string },
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

        const user_data = await request.json()

        this.loading = false;
        this.user = {
          email: user_data.email,
          name: user_data.name
        }
        this.isAuthenticated = true

        return true
      } catch(err: unknown) {
        this.loading = false
        return false;
      }
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