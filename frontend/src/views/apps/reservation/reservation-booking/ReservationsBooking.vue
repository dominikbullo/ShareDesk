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

    <b-card v-if="roomData">
      <b-card-header class="pb-50">
        <h5>
          {{ $t("Select spot") }}
        </h5>
      </b-card-header>
      <b-row>
        <b-col
          class="pt-5"
        >
          <div v-if="roomData.layout">
            <table>
              <tbody>
                <tr v-for="idxr, r in roomData.layout.rows">
                  <td
                    v-for="idxc, c in roomData.layout.columns"
                    class="pl-2"
                    style="width: 50px;"
                  >
                    <div
                      v-if="isEnabled(idxr, idxc)"
                      v-b-popover.hover.top="`${getSeat(idxr,idxc).data.identifier}`"
                      :class="classifier(idxr, idxc)"
                      style="width: 30px; height: 30px; border: 1px solid black;"
                      @click.exact="onSeatSelected(idxr, idxc, false)"
                      @click.ctrl="onSeatSelected(idxr, idxc, true)"
                    />
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </b-col>
        <b-col
          class="pt-3"
          align-content="center"
        >
          <div
            v-show="selectedSeats"
            class="card"
            style="display: none;"
          >
            <div class="card-body">
              <div v-if="selectedSeats">

                <!--TODO v for-->
                <div
                  v-for="seat in selectedSeats"
                  :key="seat.id"
                >
                  <h3>Seat data:</h3>
                  <pre> {{ seat.data }}</pre>
                  <!--                <div v-else>-->
                  <!--                  <h3>No data for this seat on the server</h3>-->
                  <!--                </div>-->

                  <div v-if="seat.reservationData.length > 0">
                    <h3>Seat reservation data:</h3>
                    <pre>{{ seat.reservationData }}</pre>
                  </div>
                  <div v-else>
                    <h3>No reservation data for this seat</h3>
                  </div>
                </div>
              </div>
            </div>

            <b-button
              v-ripple.400="'rgba(113, 102, 240, 0.15)'"
              class="ml-2"
              variant="outline-primary"
              @click="modalShow = !modalShow"
            >
              {{ $t("Book for team") }}

            </b-button>

            <!-- button -->
            <b-button
              v-ripple.400="'rgba(113, 102, 240, 0.15)'"
              class="ml-2"
              variant="outline-primary"
              @click="modalShow = !modalShow"
            >
              {{ $t("Book for user") }}
            </b-button>

            <b-button
              v-ripple.400="'rgba(113, 102, 240, 0.15)'"
              class="ml-2"
              variant="outline-primary"
              @click="modalShow = !modalShow"
            >
              {{ $t("Book for team") }}

            </b-button>

          </div></b-col>
      </b-row>
    </b-card>

    <b-row v-if="roomData">
      <!-- Spots pre zistenie, či je ten spot disabled alebo nie, resp pre layout-->
      <!--        <pre>{{ roomData }}</pre>-->
      <!-- roomSpotsReservationsData pre viac info o mieste + je ho classifier -->
      <!--        <pre>{{ roomSpotsReservationsData }}</pre>-->
      <b-col>
        <pre>{{ spots }}</pre>
      </b-col>
      <b-col>
        <pre>{{ reservations }}</pre>
      </b-col>
      <b-col>
        <pre>{{ seats }}</pre>
      </b-col>
    </b-row>
  </div>
</template>

<script>

import {
  BButton, BCard, BCardHeader, BCardText, BCol, BModal, BRow, VBTooltip, VBPopover,
} from 'bootstrap-vue'
import store from '@/store'
import Ripple from 'vue-ripple-directive'
import { onUnmounted } from '@vue/composition-api/dist/vue-composition-api'
import { compareStringNoCaseSensitive } from '@/utils/utils'
import useReservationBooking from '@/views/apps/reservation/reservation-booking/useReservationBooking'
import reservationStoreModule from '@/views/apps/reservation/reservationStoreModule'
import ReservationsListFilters from '@/views/apps/reservation/reservation-booking/ReservationsBoklingFilters.vue'
import ToastificationContent from '@core/components/toastification/ToastificationContent'

export default {
  components: {
    ReservationsListFilters,
    BCard,
    BRow,
    BCardHeader,
    BCol,
    BButton,
    BModal,
    BCardText,
  },
  directives: {
    'b-tooltip': VBTooltip,
    'b-popover': VBPopover,
    Ripple,
  },
  data() {
    return {
      modalShow: false,
      errors: [],
      o: [],
      selectedSeats: [],
      seats: [],
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
    } = useReservationBooking()

    return {
      seatStatusString: {
        booked: {
          team: 'TB',
          user: 'UB',
          permanent: 'PB',
          default: 'DB',
        },
        available: {
          full: 'FA',
          partial: 'PA',
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
    }
  },
  watch: {
    roomData(val) {
      // Generate seats on room data change
      if (this.roomData) this.generateSeats(val.layout.rows, val.layout.columns)
    },
    roomSpotsReservationsData() {
      // Generate seats on room roomSpotsReservationsData change
      if (this.roomData) this.generateSeats(this.roomData.layout.rows, this.roomData.layout.columns)
    },
  },
  created() {
    this.fetchAllWorkspaces()
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
      const seatReservation = seatReservationList[0]

      if (seatReservation.permanent) return this.seatStatusString.booked.permanent
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
        if (foundSelectedSeat === undefined) {
          return seat.status ? `cls-${seat.status.toLowerCase()}` : 'cls-fa'
        }
        if (Object.values(this.seatStatusString.booked).includes(foundSelectedSeat.status)) {
          return 'cls-booked'
        }
        if (foundSelectedSeat) {
          return 'cls-selected'
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
    onSeatSelected(r, c, multiple = false) {
      const seat = this.getSeat(r, c)
      if (this.isSeatBooked(seat)) {
        // TODO: Only show data
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
  },
}
</script>

<style lang="scss">
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
  &-tb{background-color: $secondary}
  &-ub{background-color:$secondary; border: 2px solid $primary !important;}
  &-pb{background-color:$danger}
  &-db{background-color:$secondary}
  &-fa{background-color:$light;}
  &-pa{background-color:$light;border: 2px solid $warning !important;}
}
</style>
