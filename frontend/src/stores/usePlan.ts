import type { Plan } from '@/models/plan'
import { ref, watch, computed, unref, type Ref } from 'vue'

export function usePlan(planId: number | Ref<number | null> | null) {
  const plan = ref<Plan | null>(null)
  const loading = ref(false)
  const error = ref<string | null>(null)

  watch(
    () => unref(planId),
    async (id) => {
      if (id == null) {
        plan.value = null
        return
      }

      loading.value = true
      error.value = null
      plan.value = null

      try {
        const res = await fetch(`${import.meta.env.VITE_BACKEND_URL}/plan/${id}`, {
            credentials: "include"
        })
        if (!res.ok) throw new Error(`Failed to fetch plan ${id}`)
        plan.value = await res.json()
      } catch (err: any) {
        error.value = err.message
      } finally {
        loading.value = false
      }
    },
    { immediate: true }
  )

  const hasPlan = computed(() => plan.value !== null)

  return { plan, loading, error, hasPlan }
}
