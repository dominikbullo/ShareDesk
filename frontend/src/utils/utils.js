export const addDayToDate = (dateString, days) => {
  const date = new Date(dateString)
  return new Date(date.setDate(date.getDate() + days))
}
