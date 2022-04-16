import { compareStringNoCaseSensitive } from '@/utils/utils'

export const resolveResourceType = resType => {
  if (compareStringNoCaseSensitive(resType, 'UserSpotReservation')) return 'User'
  if (compareStringNoCaseSensitive(resType, 'TeamSpotReservation')) return 'Team'
  return 'undefined'
}
