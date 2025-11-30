import type { Plan } from "@/models/plan"
import { defineStore } from "pinia"

export const usePlansStore = defineStore("plans", {
  state: () => ({
    plans: [] as Plan[],
    isLoading: false,
    error: null as string | null,
  }),

  actions: {
    async load() {
      this.isLoading = true
      this.error = null

      try {
        const data = await fetch(`${import.meta.env.VITE_BACKEND_URL}/plan`, {credentials: "include"}).then(res => res.json())
        this.plans = data
      } catch (err: any) {
        this.error = err.message || "Error fetching plans"
      } finally {
        this.isLoading = false
      }
    },
    async create(place: string, activity: string, type: string, address: string, price: string) {
      const data = await fetch(`${import.meta.env.VITE_BACKEND_URL}/plan`, {
        credentials: "include",
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          place,
          activity,
          type,
          address,
          price
        })
      })

      if(!data.ok) {
        return false;
      } else {
        return true;
      }
    }
  }
})