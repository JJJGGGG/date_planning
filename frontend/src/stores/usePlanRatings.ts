import type { Rating } from '@/models/rating'
import { ref, watch, computed, unref, type Ref } from 'vue'

export function usePlanRatings(planId: number | Ref<number | null> | null) {
  const ratings = ref<Rating[]>([])
  const rating = ref<Rating | null>(null)
  const loading = ref(false)
  const error = ref<string | null>(null)

  watch(
    () => unref(planId),
    async (id) => {
      await getAllRatings(id)
      await getMyRating(id)
    },
    { immediate: true }
  )

  async function getAllRatings(id: number | null) {
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

  }

  async function getMyRating(id: number | null) {
    if (id == null) {
      rating.value = null
      return
    }

    loading.value = true
    error.value = null
    rating.value = null

    try {
      const res = await fetch(`${import.meta.env.VITE_BACKEND_URL}/plan/${id}/my-rating`, {
          credentials: "include"
      })
      if (!res.ok) throw new Error(`Failed to fetch plan ${id}`)
      rating.value = await res.json()
    } catch (err: any) {
      error.value = err.message
    } finally {
      loading.value = false
    }
  }


  async function addRating(score: number) {
    try {
      const res = await fetch(`${import.meta.env.VITE_BACKEND_URL}/plan/${unref(planId)}/my-rating`, {
          credentials: "include",
          method: "POST",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify({
            rating: score
          })
      })
      if (!res.ok) throw new Error(`Failed to update plan rating for ${planId}`)
      rating.value = await res.json()
    } catch (err: any) {
      error.value = err.message
    } finally {
      loading.value = false
    }
  }

  return { rating, ratings, addRating, loading, error }
}
