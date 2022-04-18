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

    <spot-issue-list-add-new
      v-if="selectedSeats.length === 1"
      :is-add-new-issue-sidebar-active.sync="isAddNewIssueSidebarActive"
      :spot-id="selectedSeats[0].data.id"
    />

    <b-card
      v-if="roomData && dateFilter"
    >
      <spot-booking-legend :seat-status-string="seatStatusString" />

      <b-row class=" d-flex justify-content-center">
        <b-col
          v-if="roomData.layout"
          lg="6"
          md="12"
          class="reservation-column d-flex justify-content-center align-items-center"
        >
          <b-overlay
            :show="showSeatSpinner"
            spinner-variant="primary"
            spinner-type="grow"
            blur="1rem"
            variant="transparent"
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
                    class="table-spot"
                  >
                    <div
                      v-if="isEnabled(idxr, idxc)"
                      v-b-popover.hover.top="popoverText(idxr, idxc)"
                      :class="classifier(idxr, idxc)"
                      class="table-spot"
                      @click.exact="onSeatSelected(idxr, idxc, false)"
                      @click.ctrl="onSeatSelected(idxr, idxc, true)"
                      @click.alt="seatReservationsDetail(idxr, idxc)"
                      @click.shift="resolveSeatStatusVariant(getSeatReservationFromData(idxr, idxc))"
                    />
                  </td>
                </tr>
              </tbody>
            </table>
          </b-overlay>
        </b-col>
        <b-col
          lg="6"
          md="12"
        >
          <b-tabs
            v-if="selectedSeats && selectedSeats.length >0"
            content-class="mt-1"
          >
            <b-tab :title="$t('Reservation')">
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
                  <h5>{{ $tc("Team",1) }}</h5>
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

              <b-row class="mt-3 d-flex justify-content-end">
                <b-button
                  v-if="$can('write', 'Layout')"
                  v-ripple.400="'rgba(113, 102, 240, 0.15)'"
                  class="ml-2 mt-1 mt-md-0 btn-md-block"
                  variant="outline-danger"
                  @click="disableSpot"
                >
                  {{ `${$t("Disable")}  ${$tc("spot", selectedSeats.length)}` }}
                </b-button>

                <b-button
                  v-if="selectedSeats.length === 1"
                  v-ripple.400="'rgba(113, 102, 240, 0.15)'"
                  variant="outline-warning"
                  class="ml-2 mt-1 mt-md-0  btn-md-block"
                  @click="isAddNewIssueSidebarActive = true"
                >
                  {{ $t("Add issue") }}
                </b-button>

                <b-button
                  v-ripple.400="'rgba(113, 102, 240, 0.15)'"
                  variant="primary"
                  class="ml-2 mt-1 mt-md-0  btn-md-block"
                  @click="submitReservation"
                >
                  {{ `${$t("Book")}  ${$tc("spot", selectedSeats.length)}` }}
                </b-button>
              </b-row>
            </b-tab>
            <!--            <b-tab :title="$t('Information')">-->
            <!--              <table class="mt-2 mt-xl-0 w-100">-->
            <!--                <tr>-->
            <!--                  <th class="pb-50">-->
            <!--                    <feather-icon-->
            <!--                      icon="UserIcon"-->
            <!--                      class="mr-75"-->
            <!--                    />-->
            <!--                    <span class="font-weight-bold">{{ $t('Workspace') }}</span>-->
            <!--                  </th>-->
            <!--                  <td class="pb-50">-->
            <!--                    {{ selectedSeats }}-->
            <!--                  </td>-->
            <!--                </tr>-->
            <!--                <tr>-->
            <!--                  <th class="pb-50">-->
            <!--                    <feather-icon-->
            <!--                      icon="CheckIcon"-->
            <!--                      class="mr-75"-->
            <!--                    />-->
            <!--                    <span class="font-weight-bold">{{ $t('Floor') }}</span>-->
            <!--                  </th>-->
            <!--                  <td class="pb-50 text-capitalize">-->
            <!--                    {{ selectedSeats }}-->
            <!--                  </td>-->
            <!--                </tr>-->
            <!--                <tr>-->
            <!--                  <th class="pb-50">-->
            <!--                    <feather-icon-->
            <!--                      icon="FlagIcon"-->
            <!--                      class="mr-75"-->
            <!--                    />-->
            <!--                    <span class="font-weight-bold">{{ $t("Room") }}</span>-->
            <!--                  </th>-->
            <!--                  <td class="pb-50 text-capitalize">-->
            <!--                    {{ selectedSeats }}-->
            <!--                  </td>-->
            <!--                </tr>-->
            <!--                <tr>-->
            <!--                  <th class="pb-50">-->
            <!--                    <feather-icon-->
            <!--                      icon="CalendarIcon"-->
            <!--                      class="mr-75"-->
            <!--                    />-->
            <!--                    <span class="font-weight-bold">{{ $t('Registration time') }}</span>-->
            <!--                  </th>-->
            <!--                  <td class="pb-50">-->
            <!--                    {{ selectedSeats }}-->
            <!--                  </td>-->
            <!--                </tr>-->
            <!--              </table>-->
            <!--              <pre>{{ selectedSeats }}</pre>-->
            <!--            </b-tab>-->
          </b-tabs>
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
  BButton, BOverlay, BCard, BFormCheckbox, BCardText, BCol, BTabs, BTab, BAlert, BModal, BRow, BTable, VBPopover,
} from 'bootstrap-vue'
import store from '@/store'
import Ripple from 'vue-ripple-directive'
import { onUnmounted, ref, watch } from '@vue/composition-api/dist/vue-composition-api'
import { isTouch } from '@/utils/utils'
import useSpotBooking from '@/views/apps/reservation/spot-reservation/useSpotBooking'
import ReservationsListFilters from '@/views/apps/reservation/spot-reservation/SpotBookingFilters.vue'
import ToastificationContent from '@core/components/toastification/ToastificationContent.vue'

import flatPickr from 'vue-flatpickr-component'
import { Slovak } from 'flatpickr/dist/l10n/sk.js'
import vSelect from 'vue-select'
import { getUserData } from '@/auth/utils'

import axios from '@/libs/axios'
import SpotIssueListAddNew from '@/views/apps/workplace/issues-list/SpotIssueListAddNew.vue'
import workspaceStoreModule from '@/views/apps/workplace/workspaceStoreModule'
import { isResourceTypeTeam } from '@/views/apps/team/teamUtils'
import SpotBookingLegend from '@/views/apps/reservation/spot-reservation/SpotBookingLegend'
import { seatStatusString } from '@/views/apps/reservation/reservationsUtils'
import { formatDate } from '@/utils/filter'

export default {
  components: {
    ReservationsListFilters,
    SpotIssueListAddNew,
    SpotBookingLegend,

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
    BTabs,
    BTab,
    BAlert,
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
    const WORKSPACE_APP_STORE_MODULE_NAME = 'app-workspace'

    // Register module
    if (!store.hasModule(WORKSPACE_APP_STORE_MODULE_NAME)) store.registerModule(WORKSPACE_APP_STORE_MODULE_NAME, workspaceStoreModule)

    // UnRegister on leave
    onUnmounted(() => {
      if (store.hasModule(WORKSPACE_APP_STORE_MODULE_NAME)) store.unregisterModule(WORKSPACE_APP_STORE_MODULE_NAME)
    })

    const isAddNewIssueSidebarActive = ref(false)

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
    } = useSpotBooking()

    return {
      seatStatuses: [],
      seatStatusString,
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
      isAddNewIssueSidebarActive,
    }
  },
  watch: {
    dateFilter(val) {
      this.selectedSeats = []
      if (!val) return
      this.newReservationData.start = new Date(val).setHours(8)
      this.newReservationData.end = new Date(val).setHours(16)

      this.reservationMeta.start = new Date(val).setHours(8)
      this.reservationMeta.end = new Date(val).setHours(16)
    },
    roomData(val) {
      this.selectedSeats = []
      if (this.roomData) this.generateSeats(val.layout.rows, val.layout.columns)
    },
    roomSpotsReservationsData() {
      if (this.roomData) this.generateSeats(this.rows, this.cols)
    },
  },
  created() {
    this.fetchAllWorkspaces()
    axios
      .get('/teams/')
      .then(response => {
        this.newReservationData.teamOptions = response.data.results
      })
  },
  methods: {
    popoverText(r, c) {
      const seat = this.getSeat(r, c)
      if (!seat || !seat.data) return ''
      if (this.$ability.can('write', 'Reservation')) {
        return `${seat.data.identifier} | ${seat.status}`
      }
      return seat.data.identifier
    },
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
    resolveSeatStatusVariant(seatReservationList) {
      // potrebujem vedieť, či je to permanentná alebo nie
      // ak nie tak pozerám na každú a vyhodnocujem

      // daj preč zamietnute permanentne, tie nás nezaujímajú
      const filteredSeatReservationList = seatReservationList.filter(seatReservation => seatReservation.permanent_status !== 'rejected')
      let resolvedStatusVariant = this.seatStatusString.booked.user

      const totalAvailableTimeInDay = Math.abs(new Date(this.reservationMeta.end) - new Date(this.reservationMeta.start))
      let availableTimeInDay = totalAvailableTimeInDay
      const thresholdTimeMilliseconds = 1 * 60 * 60 * 1000

      // If there are no valid reservations
      if (filteredSeatReservationList.length <= 0) return this.seatStatusString.available.full

      for (let i = 0; i < filteredSeatReservationList.length; i++) {
        const seatReservation = filteredSeatReservationList[i]

        if (seatReservation.permanent) {
          if (seatReservation.permanent_status === 'submitted') return this.seatStatusString.booked.permanent_submitted
          if (seatReservation.permanent_status === 'allowed') return this.seatStatusString.booked.permanent_allowed
        }

        const selectedDate = new Date(this.dateFilter)
        let calcTimeStart = new Date(seatReservation.reservation.start)
        let calcTimeEnd = new Date(seatReservation.reservation.end)

        if (new Date(seatReservation.reservation.start) < selectedDate.setHours(8)) {
          calcTimeStart = selectedDate.setHours(8)
        }
        if (new Date(seatReservation.reservation.end) > selectedDate.setHours(16)) {
          calcTimeEnd = selectedDate.setHours(16)
        }
        availableTimeInDay -= Math.abs(calcTimeEnd - calcTimeStart)

        if (isResourceTypeTeam(seatReservation.resourcetype)) resolvedStatusVariant = this.seatStatusString.booked.team
      }

      if (availableTimeInDay > thresholdTimeMilliseconds) return this.seatStatusString.available.partial

      return resolvedStatusVariant
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
      return 'cls-disabled'
    },
    getSeatFromData(r, c) {
      return this.spots.filter(spot => (spot.row === r && spot.column === c))[0]
    },
    getSeatReservationFromData(r, c) {
      if (!this.roomSpotsReservationsData || this.roomSpotsReservationsData.length <= 0) return []
      // Pozor na toom, lebo ten spot síce v tej rezervacií byť môže ale v inej room
      return this.roomSpotsReservationsData.filter(element => element.spots.filter(item => (item.room === this.roomFilter && item.row === r && item.column === c)).length > 0)
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
        }
        this.seatReservationsDetail(r, c)
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
    disableSpot() {
      this.$bvModal
        .msgBoxConfirm("Please confirm you're decision", {
          title: this.$t('Please confirm'),
          size: 'sm',
          okVariant: 'danger',
          okTitle: this.$t('Delete seats'),
          cancelVariant: 'outline-secondary',
          hideHeaderClose: false,
          centered: true,
        })
        .then(value => {
          if (value) {
            axios
              .post('/spots/enabled/', { spots: this.selectedSeats.map(item => item.data.id) })
              .then(response => {
                // Not delete but replace status
                this.seats.filter(i => this.selectedSeats.filter(y => y.data.id === i.data.id).length).forEach(el => {
                  el.data.enabled = false
                })
                this.selectedSeats = []
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
          }
        })
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

      this.$bvModal
        .msgBoxConfirm("Please confirm you're reservation", {
          title: this.$t('Please confirm'),
          size: 'sm',
          okVariant: 'primary',
          okTitle: this.$t('Book'),
          cancelVariant: 'outline-secondary',
          hideHeaderClose: false,
          centered: true,
        })
        .then(value => {
          if (value) {
            axios
              .post('/reservations/', { ...data })
              .then(response => {
                this.roomSpotsReservationsData.push(response.data)
                this.selectedSeats = []
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
                      text: "You're  reservation has been created.",
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
          }
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

.reservation-column {
  min-height: 350px;
}
$reservation-light: #d5d5d5;

.cls {
  &-booked {background-color: $danger;}
  &-available {background-color: $reservation-light;}
  &-selected{background-color:$success;}
  &-tb{background-color: $secondary;}
  &-ub{background-color:$secondary; border: 2px solid $primary !important;}
  &-pb{background-color:$danger;}
  &-db{background-color:$secondary;}
  &-fa{background-color:$reservation-light;}
  &-pa{background-color:$reservation-light;border: 2px solid $warning !important;}
  &-pb{
    &-a{background-color:$danger; }
    &-s{background-color:$secondary;border: 2px solid $danger !important;}
    &-r{background-color: $reservation-light;}
  }
}

.table-spot{
  width: 30px; height: 30px; padding: 3px;
}

@media (max-width: 576px) {
  .table-spot{
    div{
      width: 100%;
      height: 100%;
    }
  }
}
</style>
