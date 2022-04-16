import { Ability } from '@casl/ability'
import { getAbilityForUserRole } from '@/auth/utils'
import { initialAbility } from './config'

//  Read ability from localStorage
// * Handles auto fetching previous abilities if already logged in user
// ? You can update this if you store user abilities to more secure place
// ! Anyone can update localStorage so be careful and please update this
const userData = JSON.parse(localStorage.getItem('userData'))

let existingAbility = null

if (userData && userData.role) {
  existingAbility = getAbilityForUserRole(userData.role)
}

if (userData && userData.ability) existingAbility = userData.ability

// original code, based od server side
// const existingAbility = userData ? userData.ability : null

export default new Ability(existingAbility || initialAbility)
