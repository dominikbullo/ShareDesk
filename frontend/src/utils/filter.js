import i18n from '@/libs/i18n'

export const formatDate = (value, formatting = { month: 'numeric', day: 'numeric', year: 'numeric' }) => {
  if (!value) return value
  return i18n.d(new Date(value), formatting)
}
