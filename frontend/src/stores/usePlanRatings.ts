import type { Rating } from '@/models/rating'
import { ref, watch, computed, unref, type Ref } from 'vue'

export function usePlanRatings(planId: number | Ref<number | null> | null) {
  const ratings = ref<Rating[]>([])
  const loading = ref(false)
  const error = ref<string | null>(null)

  watch(
    () => unref(planId),
    async (id) => {
      if (id == null) {
        ratings.value = []
        return
      }

      loading.value = true
      error.value = null
      ratings.value = []

      try {
        const res = await fetch(`${import.meta.env.VITE_BACKEND_URL}/plan/${id}/ratings`, {
            credentials: "include"
        })
        if (!res.ok) throw new Error(`Failed to fetch plan ${id}`)
        ratings.value = await res.json()
      } catch (err: any) {
        error.value = err.message
      } finally {
        loading.value = false
      }
    },
    { immediate: true }
  )

  return { ratings, loading, error }
}
