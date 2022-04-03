<template>
  <div>
    <reservations-list-filters
      :date-filter.sync="dateFilter"
      :workspace-filter.sync="workspaceFilter"
      :floor-filter.sync="floorFilter"
      :room-filter.sync="roomFilter"
      :workspace-options="workspacesList"
      :floor-options="floorsList"
      :room-options="roomsList"
    />

    <b-card
      v-if="roomData"
      class="card-body"
    >
      <b-row>
        <h1>asd</h1>
        <pre>{{ seatStatuses }}</pre>
      </b-row>
      <b-row>
        <b-overlay
          :show="showSeatSpinner"
          spinner-variant="primary"
          spinner-type="grow"
          blur="1rem"
          variant="transparent"
        >
          <b-col
            v-if="roomData.layout"
            class="col-md-auto p-5"
          >
            <b-row
              v-if="isTouch()"
              class="mb-2 d-flex justify-content-center"
              align-self="center"
            >
              <b-form-checkbox
                v-model="multipleTouchCheckbox"
                switch
                inline
                class="mb-2 text-center"
                align-self="center"
              >
                {{ $t("Mutliselect") }}
              </b-form-checkbox>
            </b-row>
            <table>
              <tbody>
                <tr v-for="idxr, r in roomData.layout.rows">
                  <td
                    v-for="idxc, c in roomData.layout.columns"
                    class="pl-1"
                    style="width: 1rem;"
                  >
                    <div
                      v-if="isEnabled(idxr, idxc)"
                      v-b-popover.hover.top="`${getSeat(idxr,idxc).data.identifier}`"
                      :class="classifier(idxr, idxc)"
                      style="width: 30px; height: 30px; border: 1px solid black;"
                      @click.exact="onSeatSelected(idxr, idxc, false)"
                      @click.ctrl="onSeatSelected(idxr, idxc, true)"
                      @click.alt="seatReservationsDetail(idxr, idxc)"
                    />
                  </td>
                </tr>
              </tbody>
            </table>
          </b-col>
        </b-overlay>
        <b-col
          class="pt-3 pl-2"
          align-content="center"
        >
          <div
            v-show="selectedSeats && selectedSeats.length >0"
            class="card"
            style="display: none;"
          >

            <div v-if="selectedSeats && selectedSeats.length >0">
              <!--TODO v for-->
              <b-row class="mb-2">
                <b-col>
                  <h5>{{ $t("Start") }}</h5>
                  <flat-pickr
                    v-model="newReservationData.start"
                    class="form-control"
                    :config="datePickerConfig"
                  />
                </b-col>
                <b-col>
                  <h5>{{ $t("End") }}</h5>
                  <flat-pickr
                    v-model="newReservationData.end"
                    class="form-control"
                    :config="datePickerConfig"
                  />
                </b-col>
              </b-row>
              <b-row
                class="mt-5"
                align-v="center"
              >
                <b-col>
                  <h5>{{ $t("Team") }}</h5>
                  <v-select
                    v-model="newReservationData.teamFilter"
                    :options="newReservationData.teamOptions"
                    class="w-100"
                    label="name"
                    :clearable="true"
                    :reduce="val => val.id"
                  />
                </b-col>
                <b-col>
                  <b-form-checkbox
                    v-model="newReservationData.permanent"
                    name="check-button"
                    switch
                    inline
                  >
                    {{ $t("Permanent") }}
                  </b-form-checkbox>
                </b-col>
              </b-row>
            </div>

            <b-row class="mt-3 justify-content-end">
              <b-button
                v-ripple.400="'rgba(113, 102, 240, 0.15)'"
                variant="outline-danger"
              >
                {{ `${$t("Disable")}  ${$tc("spot", selectedSeats.length)}` }}
              </b-button>

              <b-button
                v-ripple.400="'rgba(113, 102, 240, 0.15)'"
                variant="primary"
                class="mx-2"
                @click="submitReservation"
              >
                {{ `${$t("Book")}  ${$tc("spot", selectedSeats.length)}` }}
              </b-button>
            </b-row>

          </div>
        </b-col>
      </b-row>
    </b-card>

    <b-modal
      v-model="modalShow"
      centered
      title="Reservation data for selected seat"
      ok-only
      size="lg"
    >
      <b-card-text>
        <b-table
          responsive="sm"
          :fields="['reservation.start', 'reservation.end', 'permanent', 'resourcetype']"
          :items="modalData"
        />
      </b-card-text>
    </b-modal>
  </div>
</template>

<script>

import {
  BButton, BOverlay, BCard, BFormCheckbox, BCardText, BCol, BModal, BRow, BTable, VBPopover,
} from 'bootstrap-vue'
import store from '@/store'
import Ripple from 'vue-ripple-directive'
import { onUnmounted } from '@vue/composition-api/dist/vue-composition-api'
import { compareStringNoCaseSensitive, isTouch } from '@/utils/utils'
import useReservationBooking from '@/views/apps/reservation/reservation-booking/useReservationBooking'
import reservationStoreModule from '@/views/apps/reservation/reservationStoreModule'
import ReservationsListFilters from '@/views/apps/reservation/reservation-booking/ReservationsBoklingFilters.vue'
import ToastificationContent from '@core/components/toastification/ToastificationContent.vue'

import flatPickr from 'vue-flatpickr-component'
import { Slovak } from 'flatpickr/dist/l10n/sk.js'
import vSelect from 'vue-select'
import { getUserData } from '@/auth/utils'
import axios from '@/libs/axios'

export default {
  components: {
    ReservationsListFilters,
    BCard,
    BRow,
    BFormCheckbox,
    BOverlay,
    flatPickr,
    BCol,
    BButton,
    BModal,
    BTable,
    BCardText,
    vSelect,
  },
  directives: {
    'b-popover': VBPopover,
    Ripple,
  },
  data() {
    return {
      isTouch,
      multipleTouchCheckbox: false,

      reservationMeta: {
        start: '8:00',
        end: '18:00',
      },

      seats: [],
      modalShow: false,
      modalData: '',

      errors: [],

      selectedSeats: [],
      selectedBookedSeat: null,

      newReservationData: {
        start: '',
        end: '',
        teamFilter: null,
        teamOptions: [],
        permanent: false,
      },

      datePickerConfig: {
        locale: Slovak,
        enableTime: true,
        time_24hr: true,
        altInput: true,
        allowInput: true,
        altFormat: 'd.m.Y H:i',
        minDate: new Date(),
        defaultDate: new Date().fp_incr(1),
      },
    }
  },
  computed: {
    rows() {
      return this.roomData.layout.rows
    },
    cols() {
      return this.roomData.layout.columns
    },
    spots() {
      return this.roomData.spots
    },
    reservations() {
      return this.roomSpotsReservationsData
    },
  },
  setup() {
    const RESERVATIONS_APP_STORE_MODULE_NAME = 'app-workspace'

    // Register module
    if (!store.hasModule(RESERVATIONS_APP_STORE_MODULE_NAME)) store.registerModule(RESERVATIONS_APP_STORE_MODULE_NAME, reservationStoreModule)

    // UnRegister on leave
    onUnmounted(() => {
      if (store.hasModule(RESERVATIONS_APP_STORE_MODULE_NAME)) store.unregisterModule(RESERVATIONS_APP_STORE_MODULE_NAME)
    })

    const {
      fetchAllWorkspaces,

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

      // UI
      showSeatSpinner,
    } = useReservationBooking()

    return {
      seatStatuses: [],
      seatStatusString: {
        booked: {
          team: 'TB',
          user: 'UB',
          permanent_pending: 'PB-P',
          permanent_allowed: 'PB-A',
        },
        available: {
          full: 'FA',
          partial: 'PA',
          permanent_rejected: 'PB-R',
        },
      },
      fetchAllWorkspaces,

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

      // UI
      showSeatSpinner,
    }
  },
  watch: {
    dateFilter(val) {
      this.newReservationData.start = new Date(val).setHours(8)
      this.newReservationData.end = new Date(val).setHours(16)
    },
    roomData(val) {
      this.selectedSeats = []
      if (this.roomData) this.generateSeats(val.layout.rows, val.layout.columns)
    },
    roomSpotsReservationsData() {
      if (this.roomData) this.generateSeats(this.roomData.layout.rows, this.roomData.layout.columns)
    },
  },
  created() {
    this.fetchAllWorkspaces()
    axios
      .get('/teams/')
      .then(response => {
        this.newReservationData.teamOptions = response.data.results
      })

    const iterate = obj => {
      Object.keys(obj).forEach(key => {
        if (typeof obj[key] !== 'object') {
          this.seatStatuses.push(obj[key])
        }
        if (typeof obj[key] === 'object' && obj[key] !== null) {
          iterate(obj[key])
        }
      })
    }
    iterate(this.seatStatusString)
  },
  methods: {
    getSeat(r, c) {
      for (let i = 0; i < this.seats.length; i++) {
        if (this.seats[i].position.r == r && this.seats[i].position.c == c) {
          return this.seats[i]
        }
      }
      return null
    },
    isEnabled(r, c) {
      const seat = this.getSeatFromData(r, c)
      return seat ? seat.enabled : true
    },
    resolveSeatStatusVariant(seatReservationList) {
      // TODO better decisions and statuses for example by dates, or multiple events
      // console.log('seatReservationList')
      // console.log(seatReservationList)
      const seatReservation = seatReservationList[0]

      for (let i = 0; i < seatReservationList.length; i++) {
        console.log(seatReservationList[i])
      }
      if (seatReservation.permanent) {
        switch (seatReservation.permanent_status) {
          case 'pending':
            return this.seatStatusString.booked.permanent_pending
          case 'allowed':
            return this.seatStatusString.booked.permanent_allowed
          case 'rejected':
            return this.seatStatusString.available.permanent_rejected
          default:
            return this.seatStatusString.booked.permanent_pending
        }
      }

      if (compareStringNoCaseSensitive(seatReservation.resourcetype, 'UserSpotReservation')) return this.seatStatusString.booked.user
      if (compareStringNoCaseSensitive(seatReservation.resourcetype, 'TeamSpotReservation')) return this.seatStatusString.booked.team
      return this.seatStatusString.booked.default
    },
    generateSeats(r, c) {
      this.seats = []
      for (let y = 1; y <= r; ++y) {
        for (let x = 1; x <= c; ++x) {
          const seatReservation = this.getSeatReservationFromData(y, x)
          const seatData = this.getSeatFromData(y, x)
          if (seatReservation.length > 0) {
            this.seats.push({
              position: { r: y, c: x },
              status: this.resolveSeatStatusVariant(seatReservation),
              reservationData: seatReservation,
              data: seatData,
            })
          } else {
            this.seats.push({
              position: { r: y, c: x },
              status: this.seatStatusString.available.full,
              reservationData: [],
              data: seatData,
            })
          }
        }
      }
    },
    classifier(r, c) {
      const seat = this.getSeat(r, c)
      if (seat != null) {
        const foundSelectedSeat = this.selectedSeats.find(e => e === seat)
        if (foundSelectedSeat) {
          return 'cls-selected'
        }
        if (foundSelectedSeat === undefined) {
          return seat.status ? `cls-${seat.status.toLowerCase()}` : 'cls-fa'
        }
        if (Object.values(this.seatStatusString.booked).includes(foundSelectedSeat.status)) {
          return 'cls-booked'
        }

        return 'cls-available'
      }
    },
    getSeatFromData(r, c) {
      return this.spots.filter(spot => (spot.row === r && spot.column === c))[0]
    },
    getSeatReservationFromData(r, c) {
      if (!this.roomSpotsReservationsData || this.roomSpotsReservationsData.length <= 0) return []
      // Pozor na toom, lebo ten spot síce v tej rezervacií byť môže ale v inej room
      return this.roomSpotsReservationsData.filter(element => element.spots.filter(item => (item.room === this.roomFilter && item.row === r && item.column === c)).length > 0)
    },
    isInReservationData(r, c) {
      return this.roomSpotsReservationsData.filter(item => (item.spots.room === this.roomFilter && item.spots.row === r && item.spots.column === c))
    },
    isInSeatData(r, c) {
      return this.spots.filter(spot => (spot.row === r && spot.column === c)) > 0
    },
    isSeatBooked(seat) {
      return (Object.values(this.seatStatusString.booked).includes(seat.status))
    },
    isDatepickerValid() {
      if (!this.dateFilter) {
        this.$toast({
          component: ToastificationContent,
          props: {
            title: 'Missing date',
            icon: 'AlertTriangleIcon',
            text: 'Please select date',
            variant: 'danger',
          },
        })
        return false
      }
      return true
    },
    seatReservationsDetail(r, c) {
      if (!this.isDatepickerValid()) return
      const seat = this.getSeat(r, c)
      if (seat.reservationData && seat.reservationData.length > 0) {
        this.modalShow = true
        this.modalData = seat.reservationData
      }
    },
    onSeatSelected(r, c, multiple = false) {
      // support for touch devices
      // eslint-disable-next-line no-param-reassign
      if (this.multipleTouchCheckbox) { multiple = true }

      if (!this.isDatepickerValid()) return
      const seat = this.getSeat(r, c)
      if (this.isSeatBooked(seat)) {
        // TODO: Only show data
        console.log('seat.status')
        console.log(seat.status)
        if (seat.status === this.seatStatusString.booked.permanent_allowed) {
          this.$toast({
            component: ToastificationContent,
            props: {
              title: 'Permanent reservation',
              icon: 'EditIcon',
              text: 'This seat is reserved permanently',
              variant: 'danger',
            },
          })
          this.seatReservationsDetail(r, c)
        } else {
          this.$toast({
            component: ToastificationContent,
            props: {
              title: 'Partially reserved',
              icon: 'EditIcon',
              text: 'This seat is partially reserved',
              variant: 'warning',
            },
          })
        }
        return
      }
      if (multiple) {
        const seatIndex = this.selectedSeats.findIndex(item => item === seat)
        if (seatIndex <= -1) {
          this.selectedSeats.push(seat)
        } else {
          this.selectedSeats.splice(seatIndex, 1)
        }
      } else {
        this.selectedSeats = [seat]
      }
    },
    submitReservation() {
      const data = {
        reservation: {
          start: new Date(this.newReservationData.start).toISOString(),
          end: new Date(this.newReservationData.end).toISOString(),
        },
        created_by: getUserData().id,
        resourcetype: this.newReservationData.teamFilter ? 'TeamSpotReservation' : 'UserSpotReservation',
        reservation_for: this.newReservationData.teamFilter ? this.newReservationData.teamFilter : getUserData().id,
        spots: this.selectedSeats.map(item => item.data.id),
        permanent: this.newReservationData.permanent,
      }
      console.log(data)

      axios
        .post('/reservations/', { ...data })
        .then(response => {
          this.roomSpotsReservationsData.push(response.data)
          if (response.data.permanent) {
            this.$toast({
              component: ToastificationContent,
              props: {
                title: 'Reservation created',
                icon: 'EditIcon',
                text: "You're permanent reservation has been submitted. Now is waiting for allowance",
                variant: 'warning',
              },
            })
          } else {
            this.$toast({
              component: ToastificationContent,
              props: {
                title: 'Reservation created',
                icon: 'EditIcon',
                variant: 'success',
              },
            })
          }
        })
        .catch(error => {
          this.$toast({
            component: ToastificationContent,
            props: {
              title: 'Notification',
              icon: 'AlertTriangleIcon',
              text: 'Cannot create reservation with selected data',
              variant: 'danger',
            },
          })
          console.error(error)
        })
    },
  },
}
</script>

<style lang="scss">
@import '@core/scss/vue/libs/vue-select.scss';
@import '@core/scss/vue/libs/vue-flatpicker.scss';

// Core variables and mixins
@import '~@core/scss/base/bootstrap-extended/include';
// Overrides user variable
@import '~@core/scss/base/components/include';
// good table variable override to change the color of table

.full-width .card-header-tabs {
  margin-right: -21px;
  margin-left: -21px;
}

.full-width .nav-tabs .nav-item {
  margin-bottom: -1px;
  flex-grow: 1;
  text-align: center;
}

.cls {
  &-booked {background-color: $danger;}
  &-available {background-color: $white;}
  &-selected{background-color:$success;}
  &-tb{background-color: $secondary;}
  &-ub{background-color:$secondary; border: 2px solid $primary !important;}
  &-pb{background-color:$danger;}
  &-db{background-color:$secondary;}
  &-fa{background-color:$light;}
    &-pa{background-color:$light;border: 2px solid $warning !important;}
  &-pb{
    &-a{background-color:$danger; }
    &-p{background-color:$secondary;border: 2px solid $danger !important;}
    &-r{background-color: $white;border: 2px solid $warning !important;}
  }
}
</style>
