export const addDayToDate = (dateString, days) => {
  const date = new Date(dateString)
  return new Date(date.setDate(date.getDate() + days))
}

export const compareStringNoCaseSensitive = (a, b) => (typeof a === 'string' && typeof b === 'string'
  ? a.localeCompare(b, undefined, { sensitivity: 'accent' }) === 0
  : a === b)
