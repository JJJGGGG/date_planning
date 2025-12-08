import type { Plan } from "./plan"
import type { User } from "./user"

export type Rating = {
    user: User,
    plan: Plan,
    user_id: number,
    plan_id: number,
    rating: number
}