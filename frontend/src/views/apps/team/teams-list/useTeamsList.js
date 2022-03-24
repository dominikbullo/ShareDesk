import { ref, watch, computed } from '@vue/composition-api'
import { title } from '@core/utils/filter'
import { formatDate } from '@/utils/filter'

// Notification
import { useToast } from 'vue-toastification/composition'
import ToastificationContent from '@core/components/toastification/ToastificationContent.vue'
import store from '@/store'

export default function useTeamsList() {
  // Use toast
  const toast = useToast()

  const refTeamListTable = ref(null)

  // Table Handlers
  const tableColumns = [
    {
      key: 'name',
      label: 'Team Name',
      formatter: title,
      sortable: true,
    },
    {
      key: 'members_count',
      label: 'Number of members',
      sortable: false,
    },
    {
      key: 'created_at',
      label: 'Created at',
      sortable: true,
      formatter: value => formatDate(value, 'shortWithTime'),
    },
    { key: 'actions' },
  ]
  const perPage = ref(10)
  const totalTeams = ref(0)
  const currentPage = ref(1)
  const perPageOptions = [5, 10, 25, 50, 100]
  const searchQuery = ref('')
  const sortBy = ref('id')
  const isSortDirDesc = ref(true)
  const roleFilter = ref(null)
  const planFilter = ref(null)
  const statusFilter = ref(null)

  const dataMeta = computed(() => {
    const localItemsCount = refTeamListTable.value ? refTeamListTable.value.localItems.length : 0
    return {
      from: perPage.value * (currentPage.value - 1) + (localItemsCount ? 1 : 0),
      to: perPage.value * (currentPage.value - 1) + localItemsCount,
      of: totalTeams.value,
    }
  })

  const refetchData = () => {
    refTeamListTable.value.refresh()
  }

  watch([currentPage, perPage, searchQuery, roleFilter, planFilter, statusFilter], () => {
    refetchData()
  })

  const fetchTeams = (ctx, callback) => {
    store
      .dispatch('app-team/fetchTeams', {
        search: searchQuery.value,
        perPage: perPage.value,
        page: currentPage.value,
        ordering: isSortDirDesc.value ? sortBy.value : `-${sortBy.value}`,
      })
      .then(response => {
        const users = response.data.results
        callback(users)
        totalTeams.value = response.data.count
      })
      .catch(() => {
        toast({
          component: ToastificationContent,
          props: {
            title: 'Error fetching teams list',
            icon: 'AlertTriangleIcon',
            variant: 'danger',
          },
        })
      })
  }

  return {
    fetchTeams,

    tableColumns,
    perPage,
    currentPage,
    totalTeams,
    dataMeta,
    perPageOptions,
    searchQuery,
    sortBy,
    isSortDirDesc,

    refTeamListTable,

    refetchData,
  }
}
