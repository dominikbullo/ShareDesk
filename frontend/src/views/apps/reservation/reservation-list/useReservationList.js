import { ref, watch } from '@vue/composition-api'

// Notification
import { useToast } from 'vue-toastification/composition'
import ToastificationContent from '@core/components/toastification/ToastificationContent.vue'
import store from '@/store'
import router from '@/router'

export default function useReservationsList() {
  // Use toast
  const toast = useToast()

  const roomData = ref(null)

  const workspacesList = ref([])
  const floorsList = ref([])
  const roomsList = ref([])

  const dateFilter = ref(null)
  const workspaceFilter = ref(null)
  const floorFilter = ref(null)
  const roomFilter = ref(null)

  const WORKSPACE_APP_STORE_MODULE_NAME = 'app-workspace'

  const fetchWorkspaces = () => new Promise((resolve, reject) => {
    store.dispatch(`${WORKSPACE_APP_STORE_MODULE_NAME}/fetchWorkspaces`, {
      workspace: workspaceFilter.value,
      floor: floorFilter.value,
      room: roomFilter.value,
    })
      .then(response => {
        workspacesList.value = response.data
        resolve(response.data)
      })
      .catch(err => {
        toast({
          component: ToastificationContent,
          props: {
            title: 'Error fetching workspaces',
            icon: 'AlertTriangleIcon',
            variant: 'danger',
          },
        })
        reject(err)
      })
  })

  const fetchFloors = (ctx, callback) => new Promise((resolve, reject) => {
    store.dispatch(`${WORKSPACE_APP_STORE_MODULE_NAME}/fetchFloors`, {
      workspace: workspaceFilter.value,
      floor: floorFilter.value,
      room: roomFilter.value,
    })
      .then(response => {
        floorsList.value = response.data
        resolve(response.data)
      })
      .catch(err => {
        toast({
          component: ToastificationContent,
          props: {
            title: 'Error fetching floors',
            icon: 'AlertTriangleIcon',
            variant: 'danger',
          },
        })
        reject(err)
      })
  })

  const fetchRooms = (ctx, callback) => new Promise((resolve, reject) => {
    store.dispatch(`${WORKSPACE_APP_STORE_MODULE_NAME}/fetchRooms`, {
      workspace: workspaceFilter.value,
      floor: floorFilter.value,
      room: roomFilter.value,
    })
      .then(response => {
        roomsList.value = response.data
        resolve(response.data)
      })
      .catch(err => {
        toast({
          component: ToastificationContent,
          props: {
            title: 'Error fetching rooms',
            icon: 'AlertTriangleIcon',
            variant: 'danger',
          },
        })
        reject(err)
      })
  })

  function cleanFilters() {
    if (!roomsList.value.some(data => data.id === roomFilter.value)) {
      roomFilter.value = null
    }
    if (!floorsList.value.some(data => data.id === floorFilter.value)) {
      floorFilter.value = null
    }
    if (!workspacesList.value.some(data => data.id === workspaceFilter.value)) {
      workspaceFilter.value = null
    }
  }

  const fetchAllWorkspaces = () => Promise.all([fetchWorkspaces(), fetchFloors(), fetchRooms()])

  watch([dateFilter, workspaceFilter, floorFilter], () => {
    fetchAllWorkspaces().then(() => {
      cleanFilters()
    })
  })

  watch([roomFilter], () => {
    console.log('room filter change')
    fetchAllWorkspaces().then(() => {
      cleanFilters()
      store.dispatch(`${WORKSPACE_APP_STORE_MODULE_NAME}/fetchRoom`, { id: roomFilter.value })
        .then(response => {
          roomData.value = response.data
        })
        .catch(error => {
          if (error.response.status === 404) {
            roomData.value = undefined
          }
          console.error(error)
        })
    })
  })

  return {
    fetchAllWorkspaces,

    fetchWorkspaces,
    fetchFloors,
    fetchRooms,

    workspacesList,
    floorsList,
    roomsList,
    roomData,

    // Extra Filters
    dateFilter,
    workspaceFilter,
    floorFilter,
    roomFilter,
  }
}
