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
        const data = await fetch('http://localhost:8000/plan', {credentials: "include"}).then(res => res.json())
        this.plans = data
      } catch (err: any) {
        this.error = err.message || "Error fetching plans"
      } finally {
        this.isLoading = false
      }
    }
  }
})