import { ref } from '@vue/composition-api'

// Notification
import { useToast } from 'vue-toastification/composition'
import ToastificationContent from '@core/components/toastification/ToastificationContent.vue'
import store from '@/store'

// https://stackoverflow.com/questions/65831314/how-to-use-vue-i18n-translation-in-js-file
import i18n from '@/libs/i18n'

export default function useIssuesList() {
  // Use toast
  const toast = useToast()

  const refUserListTable = ref(null)

  // Table Handlers
  const tableColumns = [
    {
      label: i18n.t('Subject'),
      field: 'subject',
      filterOptions: {
        enabled: true,
        placeholder: `${i18n.t('Search')} ${i18n.t('Subject')}`,
      },
    },
    {
      label: i18n.t('Spot'),
      field: 'spot',
      filterOptions: {
        enabled: true,
        placeholder: `${i18n.t('Search')} ${i18n.t('Spot')}`,
      },
    },
    {
      label: i18n.t('Description'),
      field: 'description',
      filterOptions: {
        enabled: true,
        placeholder: `${i18n.t('Search')} ${i18n.t('Description')}`,
      },
    },
    {
      label: i18n.t('Created at'),
      field: 'created_at',
      type: 'date',
      dateInputFormat: 'yyyy-MM-dd\'T\'HH:mm:ss.SSSSSS\'Z\'',
      dateOutputFormat: 'dd.MM.yyyy HH:mm',
      filterOptions: {
        enabled: true,
        placeholder: `${i18n.t('Search')} ${i18n.t('Date')}`,
      },
    },
    {
      label: i18n.t('Status'),
      field: 'status',
      filterOptions: {
        enabled: true,
        placeholder: `${i18n.t('Search')} ${i18n.t('Status')}`,
        filterDropdownItems: [
          { value: 'submitted', text: 'Submitted' },
          { value: 'open', text: 'Open' },
          { value: 'in_progress', text: 'In progress' },
          { value: 'resolved', text: 'Resolved' },
        ],
      },
    },
    {
      label: i18n.t('Action'),
      field: 'action',
      sortable: false,
    },
  ]

  const totalIssues = ref(0)
  const issuesList = ref([])

  const fetchIssues = () => {
    store
      .dispatch('app-workspace/fetchIssues')
      .then(response => {
        issuesList.value = response.data
        totalIssues.value = response.data.length
      })
      .catch(() => {
        toast({
          component: ToastificationContent,
          props: {
            title: 'Error fetching issues list',
            icon: 'AlertTriangleIcon',
            variant: 'danger',
          },
        })
      })
  }

  function resolveIssueStatusVariantColor(status) {
    if (status === 'submitted') return 'warning'
    if (status === 'open') return 'primary'
    if (status === 'in_progress') return 'success'
    if (status === 'resolved') return 'secondary'
    return 'primary'
  }

  function resolveIssueStatusVariantText(status) {
    if (status === 'submitted') return i18n.t('Submitted')
    if (status === 'open') return i18n.t('Open')
    if (status === 'in_progress') return i18n.t('In progress')
    if (status === 'resolved') return i18n.t('Resolved')
    return 'No Status'
  }

  const resolveIssueStatusVariant = status => ({
    color: resolveIssueStatusVariantColor(status),
    text: resolveIssueStatusVariantText(status),
  })

  return {
    fetchIssues,
    issuesList,
    totalIssues,

    tableColumns,

    // UI
    resolveIssueStatusVariant,
  }
}
