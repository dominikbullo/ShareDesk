export const addDayToDate = (dateString, days) => {
  const date = new Date(dateString)
  return new Date(date.setDate(date.getDate() + days))
}

export const compareStringNoCaseSensitive = (a, b) => (typeof a === 'string' && typeof b === 'string'
  ? a.localeCompare(b, undefined, { sensitivity: 'accent' }) === 0
  : a === b)

export const joinArraysSafely = (arr1, arr2) => {
  if (arr1.length <= 0) return arr2
  if (arr2.length <= 0) return arr1
  return [...arr1, ...arr2]
}

export const isTouch = () => (('ontouchstart' in window) || (navigator.msMaxTouchPoints > 0))
