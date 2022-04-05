import { ref, watch } from '@vue/composition-api'

// Notification
import { useToast } from 'vue-toastification/composition'
import ToastificationContent from '@core/components/toastification/ToastificationContent.vue'
import store from '@/store'
import { joinArraysSafely } from '@/utils/utils'

export default function useReservationBooking() {
  // Use toast
  const toast = useToast()
  const showSeatSpinner = ref(false)

  const roomData = ref(null)
  const roomSpotsReservationsData = ref(null)

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
        workspacesList.value = []
        reject(err)
      })
  })

  const fetchFloors = () => new Promise((resolve, reject) => {
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
        floorsList.value = []
        reject(err)
      })
  })

  const fetchRooms = () => new Promise((resolve, reject) => {
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
        roomsList.value = []
        reject(err)
      })
  })

  const fetchReservations = () => new Promise((resolve, reject) => {
    store.dispatch(`${WORKSPACE_APP_STORE_MODULE_NAME}/fetchRoomSpots`, {
      room: roomFilter.value,
      permanent: false,
      reservation_start: dateFilter.value,
      reservation_end: dateFilter.value,
    })
      .then(response => {
        resolve(response.data)
      })
      .catch(err => {
        toast({
          component: ToastificationContent,
          props: {
            title: `Error fetching room ${roomFilter.value} spots data`,
            icon: 'AlertTriangleIcon',
            variant: 'danger',
          },
        })
        reject(err)
      })
  })

  const fetchPermanentReservations = () => new Promise((resolve, reject) => {
    store.dispatch(`${WORKSPACE_APP_STORE_MODULE_NAME}/fetchRoomSpots`, {
      room: roomFilter.value,
      permanent: true,
      start: dateFilter.value,
    }).then(response => {
      resolve(response.data)
    }).catch(err => {
      toast({
        component: ToastificationContent,
        props: {
          title: `Error fetching room ${roomFilter.value} spots data`,
          icon: 'AlertTriangleIcon',
          variant: 'danger',
        },
      })
      reject(err)
    })
  })

  const fetchRoomSpotsReservations = () => {
    if (!dateFilter.value) {
      roomSpotsReservationsData.value = []
      return
    }
    showSeatSpinner.value = true
    Promise.all([fetchReservations(), fetchPermanentReservations()]).then(values => {
      roomSpotsReservationsData.value = joinArraysSafely(values[0], values[1])
      showSeatSpinner.value = false
    })
  }

  const fetchRoom = () => {
    if (!roomFilter.value) {
      roomData.value = null
      return
    }
    store.dispatch(`${WORKSPACE_APP_STORE_MODULE_NAME}/fetchRoom`, { id: roomFilter.value })
      .then(response => {
        roomData.value = response.data
        fetchRoomSpotsReservations()
      })
      .catch(() => {
        toast({
          component: ToastificationContent,
          props: {
            title: `Error fetching room ${roomFilter.value}`,
            icon: 'AlertTriangleIcon',
            variant: 'danger',
          },
        })
        roomData.value = []
      })
  }

  function checkDatePicker() {
    if (!this.roomFilter && this.dateFilter) {
      toast({
        component: ToastificationContent,
        props: {
          title: 'Missing date',
          icon: 'AlertTriangleIcon',
          text: 'Please select also date',
          variant: 'warning',
        },
      })
    }
  }

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

  watch([workspaceFilter, floorFilter], () => {
    fetchAllWorkspaces().then(() => {
      cleanFilters()
    })
  })

  watch([roomFilter], () => {
    fetchRoom()
    fetchAllWorkspaces().then(() => {
      cleanFilters()
    })
  })

  watch([dateFilter], () => {
    fetchRoomSpotsReservations()
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
    roomSpotsReservationsData,

    // Extra Filters
    dateFilter,
    workspaceFilter,
    floorFilter,
    roomFilter,

    showSeatSpinner,
  }
}
