import type { User } from "@/models/user";
import { defineStore } from "pinia"

export const useUsersStore = defineStore("users", {
  state: () => ({
    users: [] as User[],
    loading: false,
    error: null as string | null,
  }),

  actions: {
    async load() {
      try {
        this.loading = true;
        const request = await fetch(`${import.meta.env.VITE_BACKEND_URL}/user`, {
          credentials: "include"
        });
        this.users = await request.json();
      } catch(err: any) {
        this.error = err.message || "Error fetching users"
      } finally {
        this.loading = false;
      }
    },
    async create(name: string, email:string, password: string, is_admin: boolean) {
      const data = await fetch(`${import.meta.env.VITE_BACKEND_URL}/user/signup`,{
        method: "POST",
        credentials: "include",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          name,
          email,
          password,
          is_admin
        })
      })
      return data.ok;
    },
    async edit(user_id: number, name: string, email: string, password: string, is_admin: boolean) {
      
    }
  }
});