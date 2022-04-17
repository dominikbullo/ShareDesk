import { compareStringNoCaseSensitive } from '@/utils/utils'

export const resolveResourceType = resType => {
  if (compareStringNoCaseSensitive(resType, 'UserSpotReservation')) return 'user'
  if (compareStringNoCaseSensitive(resType, 'TeamSpotReservation')) return 'team'
  return undefined
}

export const isResourceTypeUser = resType => resolveResourceType(resType) === 'user'
export const isResourceTypeTeam = resType => resolveResourceType(resType) === 'team'
export const isResourceType = resType => resolveResourceType(resType) === resType
