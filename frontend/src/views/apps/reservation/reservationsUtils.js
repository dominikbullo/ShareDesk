import i18n from '@/libs/i18n'

export const seatStatuses = [
  /* eslint-disable object-curly-newline */
  {
    cls: 'TB',
    is_booked: true,
    label: i18n.t('booking_statuses.booked.team'),
    is_permanent: false,
    key: 'team',
  },
  { cls: 'UB', label: i18n.t('booking_statuses.booked.user'), is_booked: true, is_permanent: false, key: 'user' },
  {
    cls: 'PB-S',
    label: i18n.t('booking_statuses.booked.permanent_submitted'),
    is_booked: true,
    is_permanent: true,
    key: 'permanent_submitted',
  },
  {
    cls: 'PB-A',
    label: i18n.t('booking_statuses.booked.permanent_allowed'),
    is_booked: true,
    is_permanent: true,
    key: 'permanent_allowed',
  },
  { cls: 'FA', label: i18n.t('booking_statuses.available.full'), is_booked: false, is_permanent: false, key: 'full' },
  {
    cls: 'PA',
    label: i18n.t('booking_statuses.available.partial'),
    is_booked: false,
    is_permanent: false,
    key: 'partial',
  },
  // { cls: 'PB-R', label: 'Available', is_booked: false, is_permanent: true, key: 'permanent_rejected' },
  /* eslint-enable  object-curly-newline */
]

// TODO: combine this
export const seatStatusString = {
  booked: {
    team: 'TB',
    user: 'UB',
    permanent_submitted: 'PB-S',
    permanent_allowed: 'PB-A',
  },
  available: {
    full: 'FA',
    partial: 'PA',
    permanent_rejected: 'PB-R',
  },
}
